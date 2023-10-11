# Kubernetes (k8s)

## [Components](https://kubernetes.io/docs/concepts/overview/components/)

![components-of-kubernetes](https://d33wubrfki0l68.cloudfront.net/2475489eaf20163ec0f54ddc1d92aa8d4c87c96b/e7c81/images/docs/components-of-kubernetes.svg)

### `Nodes`

worker machines which run Pods.

#### 1. `kubelet`

It makes sure that containers are running in a Pod. The kubelet takes a set of PodSpecs that are provided through various mechanisms (e.g. communicate directly with apiserver) and ensures that the containers described in those PodSpecs are running and healthy. The kubelet doesn't manage containers which were not created by Kubernetes.

#### 2. `kube-proxy`

kube-proxy is a network proxy, implementing part of the Kubernetes Service concept. kube-proxy maintains network rules on nodes. These network rules allow network communication to your Pods from network sessions inside or outside of your cluster.

#### 3. `Container runtime`

software that is responsible for running containers. It enables the `kubelet` to create containers with engines. (e.g. containerd, CRI-O)

### `Control Plane`

The control plane's components make global decisions about the cluster (for example, scheduling), as well as detecting and responding to cluster events (for example, starting up a new pod when a deployment's replicas field is unsatisfied). Typically control plane components are run on the same machine, and user containers are not run on this machine. In production environments, the control plane usually runs across multiple computers, providing fault-tolerance and high availability.

#### 1. `kube-apiserver`

The API server exposes an HTTP API that lets end users, different parts of your cluster, and external components communicate with one another. Most operations can be performed through the kubectl command-line interface or other command-line tools, such as kubeadm, which in turn use the API. However, you can also access the API directly using REST calls.

#### 2. [`etcd`](https://etcd.io/)

A distributed, reliable open source key-value store. In k8s cluster, it stored the data about state of the cluster. Only apiserver can directly communicate with etcd.

#### 3. `kube-scheduler`

selects a node for Pods to run on.

#### 4. `kube-controller-manager`

The controller manager is a loop that runs continuously and checks the status of the cluster to make sure things are running properly. It runs controller processes.

- `Node controller`: Responsible for noticing and responding when nodes go down.
- `Job controller`: Watches for Job objects that represent one-off tasks, then creates Pods to run those tasks to completion.
- `EndpointSlice controller`: Populates EndpointSlice objects (to provide a link between Services and Pods).
  1. Iterate through existing EndpointSlices, remove endpoints that are no longer desired and update matching endpoints that have changed.
  2. Iterate through EndpointSlices that have been modified in the first step and fill them up with any new endpoints needed.
  3. If there's still new endpoints left to add, try to fit them into a previously unchanged slice and/or create new ones.
- `ServiceAccount controller`: Create default ServiceAccounts for new namespaces.

#### 5. `cloud-controller-manager`

embeds cloud-specific control logic. The cloud-controller-manager only runs controllers that are specific to your cloud provider. If you are running Kubernetes on your own premises, or in a learning environment inside your own PC, the cluster does not have a cloud controller manager. As with the kube-controller-manager, the cloud-controller-manager combines several logically independent control loops into a single binary that you run as a single process. You can scale horizontally (run more than one copy) to improve performance or to help tolerate failures. The following controllers can have cloud provider dependencies:

- `Node controller`: For checking the cloud provider to determine if a node has been deleted in the cloud after it stops responding
- `Route controller`: For setting up routes in the underlying cloud infrastructure
- `Service controller`: For creating, updating and deleting cloud provider load balancers. See [LoadBalancer](#3-loadbalancer) for more.

## Concepts

### [EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/)

- You link an EndpointSlice to a Service by setting the `kubernetes.io/service-name` label on that EndpointSlice.
- The control plane automatically creates EndpointSlices for any Kubernetes Service that has a selector specified. These EndpointSlices include references to all the Pods that match the Service selector.
- EndpointSlices group network endpoints together by unique combinations of protocol(e.g. TCP), port number, and Service name.
- By default, the control plane creates and manages EndpointSlices to have no more than 100 endpoints each. You can configure this with the `--max-endpoints-per-slice` kube-controller-manager flag, up to a maximum of 1000.
- EndpointSlices can act as the source of truth for kube-proxy when it comes to how to route internal traffic.

### [Endpoints](https://kubernetes.io/docs/concepts/services-networking/service/#endpoints)

In the Kubernetes API, an Endpoints (the resource kind is plural) defines a list of network endpoints, typically referenced by a Service to define which Pods the traffic can be sent to.

### [Service](https://kubernetes.io/docs/concepts/services-networking/service/)

- Service exposes group of pods over a network so that clients can interact with it.
- The controller for Service continuously scans for Pods that match its selector, and then makes any necessary updates to the set of EndpointSlices for the Service.

**Types of Service:**

#### 1. ClusterIP

Exposes the Service on a cluster-internal IP. Choosing this value makes the Service only reachable from within the cluster. You can expose the Service to the public internet using an Ingress or a Gateway.

#### 2. [NodePort](example-resource-yaml/service.yaml)

Exposes the Service on each Node's IP at a static port (the NodePort). Every node in the cluster configures itself to listen on NodePort and to forward traffic to one of the ready endpoints associated with that Service.

**TODO: Use case ?**

#### 3. LoadBalancer

- Exposes the Service externally using an external load balancer. Kubernetes does not directly offer a load balancing component; you must provide one, or you can integrate your Kubernetes cluster with a cloud provider.
- Traffic from the external load balancer is directed at the backend Pods. The cloud provider decides how it is load balanced.
- To implement a Service of `type: LoadBalancer`, Kubernetes typically starts off by making the changes that are equivalent to you requesting a Service of `type: NodePort`. The cloud-controller-manager component then configures the external load balancer to forward traffic to that assigned node port.

#### 4. ExternalName

Services of type ExternalName map a Service to a DNS name.  
**TODO: Use case ?**

### [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)

Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster. Traffic routing is controlled by rules defined on the Ingress resource.

### [Ingress controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)

In order for the Ingress resource to work, the cluster must have an ingress controller running.

### [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)

A DaemonSet ensures that all (or some) Nodes run a copy of a Pod.
If the new Pod cannot fit on the node, the default scheduler may preempt (evict) some of the existing Pods based on the priority of the new Pod.

As nodes are added to the cluster, Pods are added to them. As nodes are removed from the cluster, those Pods are garbage collected. Deleting a DaemonSet will clean up the Pods it created.

Some typical uses of a DaemonSet are:

- running a cluster storage daemon on every node
- running a logs collection daemon on every node
- running a node monitoring daemon on every node

### DaemonSet vs Deployment

Use a Deployment for stateless services, like frontends, where scaling up and down the number of replicas and rolling out updates are more important than controlling exactly which host the Pod runs on. Use a DaemonSet when it is important that a copy of a Pod always run on all or certain hosts, if the DaemonSet provides node-level functionality that allows other Pods to run correctly on that particular node.

For example, network plugins often include a component that runs as a DaemonSet. The DaemonSet component makes sure that the node where it's running has working cluster networking.

### [Secret](https://kubernetes.io/docs/concepts/configuration/secret/)


### [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)

A ConfigMap allows you to decouple environment-specific configuration from your container images, so that your applications are easily portable.  

For example, imagine that you are developing an application that you can run on your own computer (for development) and in the cloud (to handle real traffic). You write the code to look in an environment variable named `DATABASE_HOST`. Locally, you set that variable to `localhost`. In the cloud, you set it to refer to a Kubernetes Service that exposes the database component to your cluster. This lets you fetch a container image running in the cloud and debug the exact same code locally if needed.  

**A ConfigMap is not designed to hold large chunks of data. The data stored in a ConfigMap cannot exceed 1 MiB.** If you need to store settings that are larger than this limit, you may want to consider mounting a volume or use a separate database or file service.

***Note:*** ConfigMap does not provide secrecy or encryption. If the data you want to store are confidential, use a [Secret](#secret) rather than a ConfigMap, or use additional (third party) tools to keep your data private.

There are four different ways that you can use a ConfigMap to configure a container inside a Pod:

1. Inside a container command and args
2. Environment variables for a container
    1. ConfigMaps consumed as environment variables are not updated automatically and require a pod restart.
3. Add a file in read-only volume, for the application to read
	1. When a ConfigMap consumed in a volume is updated, projected keys are **eventually** updated as well.
4. Write code to run inside the Pod that uses the Kubernetes API to read a ConfigMap

These different methods lend themselves to different ways of modeling the data being consumed. For the first three methods, the kubelet uses the data from the ConfigMap when it launches container(s) for a Pod.

The fourth method means you have to write code to read the ConfigMap and its data. However, because you're using the Kubernetes API directly, your application can subscribe to get updates whenever the ConfigMap changes, and react when that happens. By accessing the Kubernetes API directly, this technique also lets you access a ConfigMap in a different namespace.

A ConfigMap is an API object that lets you store configuration for other objects to use. Unlike most Kubernetes objects that have a `spec`, a ConfigMap has `data` and `binaryData` fields. These fields accept key-value pairs as their values. Both the `data` field and the `binaryData` are optional. The data field is designed to contain UTF-8 strings while the binaryData field is designed to contain binary data as base64-encoded strings.

Each key under the data or the binaryData field must consist of alphanumeric characters, `-`, `_` or `.`. The keys stored in data must not overlap with the keys in the binaryData field.

Starting from v1.19, you can add an immutable field to a ConfigMap definition to create an immutable ConfigMap.

[example-yaml](./resource-yaml/configMap.yaml)

#### [Immutable ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/#configmap-immutable)

The Kubernetes feature Immutable Secrets and ConfigMaps provides an option to set individual Secrets and ConfigMaps as immutable. For clusters that extensively use ConfigMaps (at least tens of thousands of unique ConfigMap to Pod mounts), preventing changes to their data has the following advantages:

    - protects you from accidental (or unwanted) updates that could cause applications outages
    - improves performance of your cluster by significantly reducing load on kube-apiserver, by closing watches for ConfigMaps marked as immutable.

You can create an immutable ConfigMap by setting the `immutable` field to `true`.

**Note:** Once a ConfigMap is marked as immutable, it is not possible to revert this change nor to mutate the contents of the data or the binaryData field. You can only delete and recreate the ConfigMap. Because existing Pods maintain a mount point to the deleted ConfigMap, it is recommended to recreate these pods.

## Security

### Scanning resource files (YAML) using [snyk-cli](https://docs.snyk.io/snyk-cli)

snyk-cli installation: <https://docs.snyk.io/snyk-cli/install-the-snyk-cli>

```bash
curl --compressed https://static.snyk.io/cli/latest/snyk-macos -o snyk
chmod +x ./snyk
mv ./snyk /usr/local/bin/
```

Scanning resource file
`snyk iac test tech-framework-language/k8s/resource-yaml/k8s.yaml`

## Monitoring

Install [kube-state-metrics](https://artifacthub.io/packages/helm/prometheus-community/kube-state-metrics) helm chart to generate and expose cluster-level metrics.

```bash
## install kube-state-metrics using helm
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install kube-state-metrics prometheus-community/kube-state-metrics -n metric

## start port local port forwarding to k8s pod
k port-forward svc/kube-state-metrics 8081:8080 -n metric
```

Access <http://localhost:8081/> in browser.

## Advance

### [kubectx + kubens](https://github.com/ahmetb/kubectx/)

**kubectx** is a tool to switch between contexts (clusters) on kubectl faster.  
**kubens** is a tool to switch between Kubernetes namespaces (and configure them for kubectl) easily.

#### Installation Homebrew (macOS and Linux)

```sh
brew install kubectx
```

#### Examples

```sh
# switch to another cluster that's in kubeconfig
$ kubectx minikube
Switched to context "minikube".

# switch back to previous cluster
$ kubectx -
Switched to context "oregon".

# rename context
$ kubectx dublin=gke_ahmetb_europe-west1-b_dublin
Context "gke_ahmetb_europe-west1-b_dublin" renamed to "dublin".

# change the active namespace on kubectl
$ kubens kube-system
Context "test" set.
Active namespace is "kube-system".

# go back to the previous namespace
$ kubens -
Context "test" set.
Active namespace is "default".
```
