[Sitemap](https://medium.com/sitemap/sitemap.xml)

## What is Longhorn?

**Longhorn** is an open-source distributed block storage system designed specifically for Kubernetes. It simplifies persistent storage management and provides features like automated volume provisioning, snapshots, and backups.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*6KNdbYoxUCIRWHPGKJ9K2Q.png)

## Key Features of Longhorn:

- **Built for Kubernetes**
- **Distributed Storage**
- **Snapshots and Backups**

To install Longhorn, start by adding its Helm repository

```c
helm repo add longhorn https://charts.longhorn.io
helm repo update

helm install longhorn longhorn/longhorn \
  --namespace longhorn-system \
  --create-namespace \
  --set defaultSettings.defaultReplicaCount=2 \
  --set defaultSettings.defaultDataPath="/var/lib/longhorn" \
  --set defaultSettings.defaultLonghornStaticStorageClass="longhorn"
```

Verify everything is working

```c
kubectl get pods -n longhorn-system
```

As usual, I mapped the longhorn UI to my sub-domains. using an ingress resource. I’ve already created an A-record, cluster issuer, and API token for my ingress IP address. [I detailed that process in this blog post](https://medium.com/@badex/part-3-automating-homelab-kubernetes-setup-deploying-argocd-with-metallb-nginx-ingress-454a32c1d4aa)

`**ingress.yaml**`

```c
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: longhorn-ui
  namespace: longhorn-system
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-namecom
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - longhorn.badex.dev
      secretName: longhorn-tls
  rules:
    - host: longhorn.badex.dev
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: longhorn-frontend
                port:
                  number: 80
```
```c
kubectl apply -f ingress.yaml
```

verify the ingress

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*dovK1v9ticsY3uJQN7R-FQ.png)

## Deploy MinIO

Now, I’ll walk through how I deployed MinIO, a high-performance S3-compatible object storage server, in my Kubernetes homelab. The goal was to GitOps everything using ArgoCD, expose MinIO securely via NGINX Ingress with Let’s Encrypt TLS, and persist data using NFS-backed volumes from my NAS.

Along the way, I dealt with image architecture issues, CRD mismatches, and a few failed post-install hooks — and I’ll share how I solved them too.

## What is MinIO and Why Use It in a Homelab?

When building out a Kubernetes homelab, persistent storage becomes one of the most critical concerns. Whether you’re running databases, media apps, or Kubernetes-native tools like Longhorn, you need a reliable, flexible, and scalable way to store and access data. That’s where **MinIO** comes in.

MinIO is a high-performance, S3-compatible object storage system. It brings **cloud-native storage capabilities** — like versioned buckets, access policies, and client SDKs into your **on-premise environment**. In a homelab, MinIO is especially valuable when paired with **Longhorn**, which handles persistent volumes across nodes. With MinIO acting as a backup target, Longhorn can offload volume snapshots and disaster recovery data to object storage, giving you the same resilience patterns used in production-grade cloud deployments.

By deploying MinIO using GitOps (ArgoCD), exposing it securely via NGINX and TLS, and persisting its data using NFS-backed volumes from my NAS, I’ve built a storage layer that’s not only powerful and scalable but also declaratively managed, reproducible, and secure.

## Get Taiwo Badejo’s stories in your inbox

Join Medium for free to get updates from this writer.

**My Folder structure (GitOps-Driven)**

```c
kubernetes-homelab/
├── applications/
│   ├── minio.yaml                # ArgoCD Application for MinIO Helm chart
│   └── minio-ingress.yaml        # ArgoCD Application for ingress.yaml
├── argocd-apps/
│   └── minio/
│       ├── custom-values.yaml    # Helm values override
│       ├── ingress.yaml          # Ingress to expose MinIO UI securely
│       └── kustomization.yaml
```

## 1\. Install the NFS Dynamic Provisioner

```c
helm repo add nfs-subdir-external-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner/
helm install nfs-provisioner nfs-subdir-external-provisioner/nfs-subdir-external-provisioner \
  --set nfs.server= <NAS ipaddress> \
  --set nfs.path= <path to minio on your nas>\
  --set storageClass.name=nfs \
  --set storageClass.defaultClass=false \
  --set storageClass.reclaimPolicy=Retain
```

This created a dynamic `nfs` StorageClass backed by my Synology NAS.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*L0IrGX4BZJtRfnqJiVVrvA.png)

## 2\. Create the MinIO Namespace and Credentials Secret

```c
kubectl create namespace minio
```
```c
kubectl create secret generic minio-login \
  --from-literal=rootUser=minioadmin \
  --from-literal=rootPassword=supersecurepass \
  -n minio
```

## 3\. Deploying MinIO via ArgoCD

## Step 1: Define Helm custom-values.yaml

`**argocd-apps/minio/custom-values.yaml**`

```c
nameOverride: "minio"
fullnameOverride: "minio"
mode: standalone
image:
  repository: quay.io/minio/minio
  tag: RELEASE.2023-10-25T06-33-25Z
mcImage:
  repository: quay.io/minio/mc
  tag: RELEASE.2024-11-21T17-21-54Z
rootUser: ""
rootPassword: ""
existingSecret: minio-login
persistence:
  enabled: true
  storageClass: nfs
  accessMode: ReadWriteMany
  size: 150Gi
service:
  type: ClusterIP
  port: "9000"
consoleService:
  type: ClusterIP
  port: "9001"
securityContext:
  enabled: true
  runAsUser: 65534
  runAsGroup: 100
  fsGroup: 100
  fsGroupChangePolicy: "OnRootMismatch"
metrics:
  serviceMonitor:
    enabled: true
    includeNode: true
    public: true
    namespace: minio
    interval: 60s
    scrapeTimeout: 30s
resources:
  requests:
    memory: 2Gi
    cpu: 500m
  limits:
    memory: 4Gi
    cpu: 1
```

This created a dynamic `nfs` StorageClass backed by my Synology NAS.

## Step 2: Create an Ingress resource for the MinIO Console

To access the MinIO UI via my mapped domain, I created the ingress.yaml

`**argocd-apps/minio/ingress.yaml**`

```c
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: minio-ingress
  namespace: minio
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-namecom
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
    nginx.ingress.kubernetes.io/backend-protocol: "HTTP"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - minio.badex.dev
      secretName: minio-tls
  rules:
    - host: minio.badex.dev
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: minio-console
                port:
                  number: 9001
```

## Step 3: ArgoCD Application Manifests

I’ll be creating two application manifests. The first manifest (minio.yaml) deploys MinIO via a Helm chart. The second manifest (minio-ingress.yaml) deploys the ingress resource created above, since Argo CD only recognizes application objects.

`**applications/minio.yaml**`

```c
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: minio
  namespace: argocd
spec:
  project: default
  sources:
    - repoURL: https://charts.min.io/
      chart: minio
      targetRevision: 5.4.0
      helm:
        valueFiles:
          - $values/argocd-apps/minio/custom-values.yaml
    - repoURL: https://github.com/turbo-badex/kubernetes-homelab
      targetRevision: main
      ref: values
  destination:
    server: https://kubernetes.default.svc
    namespace: minio
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

`**applications/minio-ingress.yaml**`

```c
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: minio-ingress
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/turbo-badex/kubernetes-homelab
    targetRevision: main
    path: argocd-apps/minio
    directory:
      recurse: true
  destination:
    server: https://kubernetes.default.svc
    namespace: minio
  syncPolicy: {}
```

## Step 4: Apply to the Cluster

These are optional monitoring components that the MinIO Helm chart attempts to create if metrics are enabled. Not installing these will lead to the installation failure of MinIO

```c
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack \
  --namespace monitoring --create-namespace
```

## Step 5: Apply to the Cluster

```c
kubectl apply -f applications/minio.yaml
```
```c
kubectl apply -f applications/minio-ingress.yaml
```

Ideally, you should wait a few minutes until the application from the first command is ready before running the second command. The first command triggers ArgoCD to sync the chart, apply the values, and the second command expose MinIO over HTTPS.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*nX5eese3kPPdfBtyg--Kmg.png)

## Conclusion

By integrating Longhorn and MinIO, your Kubernetes homelab gains robust, scalable storage for both persistent volumes and object-based backups. This architecture keeps your data secure, highly available, and recovery-ready — all maintained (except longhorn) through a declarative GitOps workflow.

In the next post, we’ll take it a step further by adding Prometheus and Grafana to introduce observability and monitoring into the stack.