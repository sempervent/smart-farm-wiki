One thing missing from the [homelab](https://fredrickb.com/2021/08/22/recreating-the-raspberry-pi-homelab-with-kubernetes/) was the option to provide underlying persistent storage for workloads. I looked at a few options, but ultimately landed on [Longhorn](https://longhorn.io/), which is a cloud native distributed block storage for Kubernetes.

## Hardware upgrades

Before starting to make use of Longhorn I obviously need some disks formatted and mounted to a few of the Pis that will act as storage nodes. I went with 2x [Kingston A400](https://www.kingston.com/en/ssd/a400-solid-state-drive) 2.5” SSD 240GB. There was no room left in my current case for the drives so I purchased a new case: [Upgraded Complete Enclosure for Raspberry Pi Clusters](https://www.uctronics.com/cluster-and-rack-mount/for-raspberry-pi/uctronics-upgraded-complete-enclosure-for-raspberry-pi-cluster.html) which has 4x 2.5” slots, leaving 2 slots for future expansion. For cables I got the [SSD to USB 3.0 cable](https://thepihut.com/products/ssd-to-usb-3-0-cable-for-raspberry-pi) based on the reviews and the fact that it has been tested specifically with the Raspberry Pi. The “Notes” section mentions:

- Use an SSD when connecting
- Preferably use with Raspberry Pi 4B, not 3B+ due to speed constraints with USB 2.0

This leaves 2 nodes in the cluster that qualify, which is why I only went with 2x disks for storage. This caused some headache during the [installation](#installing-longhorn) that I’ll get into later.

While the new case is an improvement, it has one drawback. Unless you’re using a PoE switch with the PoE Hat, connecting the power source over USB-C requires unfastening the mounted Pi. I wish there was an easier way of connecting to a standard power source on an already mounted Pi. Other than that the case is great, and mounting the Pis, disks, and the remaining components was a breeze. Having space for a switch inside the bottom of the case is a bonus for keeping things tidy.

## Baseline setup of storage nodes

Longhorn has a few [installation requirements](https://longhorn.io/docs/1.3.0/deploy/install/#installation-requirements) which can be automated using Ansible. This is an extracted version of the inventory and playbook I use for the storage nodes in the cluster (`hostx` represents fictitious hosts for demonstration).

This setup presumes a few things:

- There is only a single disk device on each storage node
- Disk device is represented identically on all storage nodes

I could have used `lvm` to pool disks, but all storage nodes will only ever have a single disk attached to it given the constraints of the case. I’d rather have more nodes with disks than nodes connected to multiple disks. Keeping it simple for now.

Inventory:

```js
[k3s_servers]
host1 node_name=rpi4b1

[k3s_agents]
host2 node_name=rpi4b2
host3 node_name=rpi3b1
host4 node_name=rpi3b2

[storage_servers]
host1
host2

[storage_servers:vars]
device=/dev/sda
partition=/dev/sda1
mount_point=/mnt/data
```

Playbook:

```yaml
- name: Format disks for storage before installing Longhorn
  hosts: storage_servers
  tags: longhorn
  tasks:
  - name: Partition the disk into a single large partition filling the disk
    become: yes
    parted:
      device: "{{ device }}"
      number: 1
      state: present
      part_start: "0%"
      part_end: "100%"
      unit: GB

  - name: Create filesystem on new partition
    become: yes
    filesystem:
      fstype: ext4
      dev: "{{ partition }}"

  - name: Mount drive on {{ mount_point }}
    become: yes
    mount:
      src: "{{ partition }}"
      path: "{{ mount_point }}"
      fstype: ext4
      state: mounted
      boot: yes
      backup: yes

- name: Prepare agents for Longhorn
  hosts: k3s_servers, k3s_agents
  tags: longhorn
  tasks:
  - name: Install necessary packages required by Longhorn
    become: yes
    apt:
      pkg:
      - jq
      - open-iscsi
      state: present

  - name: Start the systemd service for iscsid if it is not started
    become: yes
    systemd:
      name: iscsid
      enabled: yes
      state: started

- name: Verify prerequisites for Longhorn and label storage nodes
  hosts: k3s_servers
  tags: longhorn
  tasks:
  - name: Run the preconfig script
    become: yes
    shell: curl -sSfL https://raw.githubusercontent.com/longhorn/longhorn/v1.2.4/scripts/environment_check.sh | bash
    register: check

  - name: Print output from check
    debug: msg="{{ check.stdout }}"

  # Label the nodes to ensure Longhorn volumes are only placed on disks of the storage nodes:
  # https://longhorn.io/kb/tip-only-use-storage-on-a-set-of-nodes/#tell-longhorn-to-create-a-default-disk-on-a-specific-set-of-nodes
  - name: Apply label "node.longhorn.io/create-default-disk=true" on storage nodes in Kubernetes
    become: yes
    command: kubectl label nodes --overwrite {{ hostvars[item].node_name }} node.longhorn.io/create-default-disk=true
    loop: "{{ hostvars[inventory_hostname]['groups']['storage_servers'] }}"
```

The tasks running the preconfig script and dumping the output will take care of verifying the prerequisites. Using a curl pipe into bash as sudo is not recommended on anything thats important, use at your own risk.

## Creating backup target

I didn’t add this initially, but having a backup target in Longhorn makes sense not only in terms of data protection, but also for [cluster upgrades](#cluster-upgrades).

There are two choices when considering backup targets for Longhorn, NFS or S3. I don’t have a NAS or a [Minio](https://min.io/) instance running standalone from my cluster, so I opted for using [Object Storage from Linode](https://www.linode.com/docs/products/storage/object-storage/) as a remote backup target. Any solution compatible with S3 or NFS, whether it is self-hosted or cloud-based will do.

Once a bucket and access keys has been created, the following must be configured:

1. The Kubernetes secret holding the URL, access key and access secret of the bucket
2. The S3-formatted URL of the bucket

In my case I’m deploying Longhorn into the namespace `longhorn-system`. Longhorn expects a secret in the following format (all items are base64-encoded as with any secret, but shown in cleartext for clarity):

`secret.yaml`:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: longhorn-linode-s3-backup-credentials
  namespace: longhorn-system
type: Opaque
data:
  AWS_ENDPOINTS: "<s3-endpoint-excluding-bucket-name>" # https://<linode-region>.linodeobjects.com
  AWS_ACCESS_KEY_ID: "<access-key>" # Access Key connected to given bucket in Linode
  AWS_SECRET_ACCESS_KEY: "<access-secret>" # Access Secret connected to given bucket in Linode
```

*`AWS_ENDPOINTS` does not include the name of the bucket. This is defined in the S3-formatted URL.*

Once the secret is created, the last thing required for backups is formatting the URL of the S3-compatible bucket. This is somewhat confusing and not explained well enough in the docs, but the gist of it is to only include the name of the bucket and a placeholder for a region if you are not using S3 from AWS. This means that for any other alternative, the URL *must* have a region as a placeholder. The format of the URL is `s3://<bucket-name>@<placeholder-region>/`. The `/` at the end is required to have all backups placed at the path `/backupstore`. Append more after `/` to change the root path. Thanks to [Citrullin](https://github.com/longhorn/longhorn/issues/4205#issuecomment-1176070305) for pointing out the formatting of the URL.

To give an example of formatting the S3-URL: Say I have a bucket named `a` hosted on `us-east-1` in Linode. It does not matter what is added as region, but to keep things consistent I’ll use `us-east-1` in the URL of the Backup Target. The final URL becomes `s3://a@us-east-1/`, where `us-east-1` is just a placeholder.

These are the two pieces of information to keep for the installation process later:

1. The *name* of the secret created
2. The S3 formatted URL (`s3://<bucket-name>@<placeholder-region>/`)

## Installing Longhorn

The installation process is fairly straightforward with Helm. The entire process is captured in a script named `install.sh` displayed below. This is where the S3-formatted URL and the name of the Kubernetes secret from earlier is used. The values are added as `defaultSettings.backupTarget` and `defaultSettings.backupTargetCredentialSecret` respectively.

*Note that defining keys under `defaultSettings` in YAML [cannot be done retroactively after the initial installation in 1.2.4](https://github.com/longhorn/longhorn/issues/2570), the settings won’t take effect and must be modified in the UI or via a full reinstall of Longhorn. This has been fixed in version 1.3.0.*

`install.sh`:

```sh
#!/bin/bash

# Installs Longhorn into the cluster
# for storage.

helm repo add longhorn https://charts.longhorn.io
helm repo update
helm upgrade --install \
--version 1.2.4 \
--namespace longhorn-system \
longhorn longhorn/longhorn \
-f values.yaml \
--set-string defaultSettings.backupTarget="<s3-formatted-url-for-backups>" \
--set-string defaultSettings.backupTargetCredentialSecret="<name-of-the-secret-with-credentials>"

# Remove the default flag from the local-provisioner
# storage class which K3s adds as part of a standard
# installation since longhorn will be the default storage
# class after the installation.
kubectl patch storageclass local-path -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'
```

`values.yaml`:

```yaml
# Description of values are explained here:
# https://github.com/longhorn/charts/blob/longhorn-1.2.4/charts/longhorn/questions.yml

# This is because I want to expose the
# UI of Longhorn outside the cluster
# with an IP address. Optional.
service:
  ui:
    type: LoadBalancer

persistence:
  # Is by default 3, since there are
  # only 2 nodes in the cluster dedicated to
  # storage this must be set to 2.
  defaultClassReplicaCount: 2

# Only important if you run Prometheus
# and want to scrape metrics from Longhorn
# and display it with something like Grafana
# in a dashboard.
annotations:
  prometheus.io/scrape: "true"

defaultSettings:
  # Mountpoint of the filesystem on the two Raspberry Pis
  # dedicated to storage.
  defaultDataPath: /mnt/data
  taintToleration: node-role.kubernetes.io/master:NoSchedule
  # Ensure that only specifically labeled nodes are used for storing
  # longhorn volumes: https://longhorn.io/kb/tip-only-use-storage-on-a-set-of-nodes/#tell-longhorn-to-create-a-default-disk-on-a-specific-set-of-nodes
  createDefaultDiskLabeledNodes: true
  storageMinimalAvailablePercentage: 10
  # Ensure that volumes created from the UI
  # of Longhorn has 2 replicas set by default
  # for the same reasons persistence.defaultClassReplicaCount
  # is set to 2 instead of 3 replicas.
  defaultReplicaCount: 2

longhornManager:
  # Let the control plane nodes with
  # disks mounted be available for
  # scheduling. 
  tolerations:
  - key: ""
    operator: "Exists"
    effect: "NoSchedule"

longhornDriver:
  # Let the control plane nodes with
  # disks mounted be available for
  # scheduling.
  tolerations:
  - key: ""
    operator: "Exists"
    effect: "NoSchedule"
```

Notable values are `persistence.defaultClassReplicaCount`, `defaultSettings.defaultReplicaCount` and `defaultSettings.createDefaultDiskLabeledNodes`. By default Longhorn wants 3 replicas of volumes. With only 2 dedicated storage nodes the installation is instructed to make only 2 replicas. Both storage nodes were labeled `node.longhorn.io/create-default-disk=true` as part of the Ansible playbook. Adding that specific label in combination with the setting `defaultSettings.createDefaultDiskLabeledNodes=true` ensures replicas are only scheduled to nodes containing that specific label and excludes the rest of the nodes. This is important since by default any node in the cluster is considered to be eligible as a storage node.

At the end of the script there is a patching of the StorageClass for `local-path`:

```sh
kubectl patch storageclass local-path -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'
```

The patching of the StorageClass is only necessary since K3s ships with its own default StorageClass `local-path`. By patching the StorageClass to no longer be the default, the Longhorn StorageClass takes over as the default after the installation:

```js
NAME                 PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
local-path           rancher.io/local-path   Delete          WaitForFirstConsumer   false                  42h
longhorn (default)   driver.longhorn.io      Delete          Immediate              true                   40h
```

After the installation, any PersistentVolume created in the cluster is by default a Longhorn volume.

With Longhorn installed its time to setup two `RecurringJobs`, which are basically cron-jobs for taking snapshots and backups of Longhorn volumes which are then pushed to the Backup Target. Adding the group `default` ensures that all volumes not involved in another recurring job is automatically included by the jobs. Snapshots and backups of volumes are then taken care of by default for all volumes.

`recurring_snapshot_job.yaml` (snapshot volumes every 12 hours):

```yaml
apiVersion: longhorn.io/v1beta1
kind: RecurringJob
metadata:
  name: 12-hour-snapshots
  namespace: longhorn-system
spec:
  cron: "0 */12 * * *"
  task: "snapshot"
  groups:
  - default
  retain: 3
  concurrency: 2
  labels:
    job: 12-hour-snapshots
```

`recurring_backup_job.yaml` (backup volumes at 00:00 every day):

```yaml
apiVersion: longhorn.io/v1beta1
kind: RecurringJob
metadata:
  name: nightly-backups
  namespace: longhorn-system
spec:
  cron: "0 0 * * *"
  task: "backup"
  groups:
  - default
  retain: 3
  concurrency: 2
  labels:
    job: nightly-backups
```

Summary of what has been done up until now:

- Longhorn is installed and takes care of provisioning Longhorn volumes for any PersistentVolume using the default StorageClass in the cluster.
- All Longhorn volumes provisioned are replicated across the two storage nodes and can be attached to any node in the Kubernetes cluster.
- All volumes created in Longhorn has snapshots and backups taken, which are then pushed to an S3 bucket at regular intervals.

The last point is important, because it is the foundation of the upgrade strategy explained in the next section.

## Cluster upgrades

Rather than performing in-place upgrades of the Kubernetes cluster as new versions are released, it should be possible to treat the cluster like immutable infrastructure that can be destroyed and recreated on demand. The cluster state and the state of all workloads must be possible to reproduce after a cluster upgrade using configuration as code, scripts and restored volumes. Given that the Pis themselves are physical, I want to be able to uninstall everything, delete the disk partitions and reflash the SD-cards.

Having a remote backup of volumes used by workloads solves the issue of data migration for this upgrade strategy. An installation of Longhorn which points to the same backup target after a reinstall has access to all the backups of all volumes from the previous cluster state. PersistentVolumes and PersistentVolumeClaims can be created from those backups. As long as workloads use consistent naming of PersistentVolumeClaims they can bind to claims with the same name.

This upgrade process is reliant on all workloads in the cluster being defined as code. All workloads must be defined as YAML configuration and scripts which should be checked into version control.

The steps of the upgrade process then becomes:

1. Backup Longhorn volumes if last backup taken is too old (optional)
2. Delete all non-system namespaces (depends on how graceful the uninstall should be. Can be skipped)
3. Remove all cluster configuration and uninstall all components using an Ansible playbook, including Longhorn configuration which also deletes the disk partition
4. Change Ansible playbook used to install K3s. Bump the channel and version of Kubernetes and run the playbook which installs K3s and prepares storage nodes for Longhorn
5. Reinstall necessary system components required for Longhorn (only really needed for having access to the Longhorn UI outside, can be skipped if ClusterIP and port forwarding is used):
	1. MetalLB
6. Reinstall Longhorn and point it to the same backup target that the previous installation was using
7. Restore all volumes back into the cluster using the Longhorn UI
8. Recreate all namespaces in the cluster used by workloads
9. Create PersistentVolumes and PersistentVolumeClaims for each volume in Longhorn and deploy PersistentVolumeClaims into the correct namespaces using the Longhorn UI. Ensure naming is consistent with the workload YAML
10. Deploy all workloads to the cluster. All workloads should bind to the previously created PersistentVolumeClaims and spin up with the data from the backup

Several of these steps are redundant if [Velero](https://velero.io/) is used. There is [documentation](https://longhorn.io/docs/1.2.4/advanced-resources/cluster-restore/restore-to-a-new-cluster-using-velero/) on how to make use of Velero as part of a backup and restore strategy with Longhorn.

The upgrade process described above is how I upgraded my homelab cluster from `1.21.7` to `1.22.12`.

## Conclusion

I find Longhorn to be a fairly straightforward solution for persistent storage. There is some setup required, but I have yet to see anything listed in the docs I couldn’t automate using Ansible or Helm. The backup feature combined with RecurringJobs is a good utility for data protection, but I mainly see it as something simplifying the upgrade process of the cluster in a true “cattle not pets” fashion.

There are some things that I think will improve with better documentation and more iteration on the solution. I don’t like that finding the correct way to format URLs for an S3-compatible service not on AWS includes digging through issues and discussions on Github. The placeholder region which is required as part of the S3-formatted URL when it isn’t even used is not very intuitive. But all things considered these are small things to point out on an otherwise good solution for persistent storage in Kubernetes.