The Longhorn Documentation

Cloud native distributed block storage for Kubernetes

[Edit this page](https://github.com/longhorn/website/edit/master/content/docs/1.11.1/_index.md)

**Longhorn** is a lightweight, reliable, and powerful distributed [block storage](https://cloudacademy.com/blog/object-storage-block-storage/) system for Kubernetes.

Longhorn implements distributed block storage using containers and microservices. Longhorn creates a dedicated storage controller for each block device volume and synchronously replicates the volume across multiple replicas stored on multiple nodes. The storage controller and replicas are themselves orchestrated using Kubernetes.

## Features

- Enterprise-grade distributed block storage with no single point of failure
- Incremental snapshot of block storage
- Backup to secondary storage ([NFS](https://www.extrahop.com/resources/protocols/nfs/) or [S3](https://aws.amazon.com/s3/) -compatible object storage) built on efficient change block detection
- Recurring snapshots and backups
- Automated, non-disruptive upgrades. You can upgrade the entire Longhorn software stack without disrupting running storage volumes.
- An intuitive GUI dashboard