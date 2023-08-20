# [Helm](https://helm.sh/) - k8s package management

## Installation

```bash
# Mac
brew install helm

# Ubuntu
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
sudo apt-get install apt-transport-https --yes
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm

# Windows
choco install kubernetes-helm
```

## Helm chart

### Install chart

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install kube-state-metrics prometheus-community/kube-state-metrics -n metric
```

### [Customizing the Chart Before Installing](https://helm.sh/docs/intro/using_helm/#customizing-the-chart-before-installing)

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami

# To see what options are configurable on a chart, use helm show values
helm show values bitnami/wordpress > wordpress.yaml

# You can then override any of these settings in a YAML formatted file, and then pass that file during installation.
echo '{mariadb.auth.database: user0db, mariadb.auth.username: user0}' > wordpress.yaml
helm install -f wordpress.yaml bitnami-wordpress bitnami/wordpress

helm uninstall bitnami-wordpress
```

### Handling whitespace

`{{-` (with the dash and space added) indicates that whitespace should be chomped left, while `-}}` means whitespace to the right should be consumed. Be careful! Newlines are whitespace!

> Make sure there is a space between the `-` and the rest of your directive. `{{- 3 }}` means "trim left whitespace and print 3" while `{{-3 }}` means "print -3".

Just for the sake of making this point clear, an `*` for each whitespace that will be deleted following this rule. An `*` at the end of the line indicates a newline character that would be removed in below yaml.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
data:
  myvalue: "Hello World"
  drink: {{ .Values.favorite.drink | default "tea" | quote }}
  food: {{ .Values.favorite.food | upper | quote }}*
**{{- if eq .Values.favorite.drink "coffee" }}
  mug: "true"*
**{{- end }}
```


### [if-else](https://helm.sh/docs/chart_template_guide/control_structures/#ifelse)

```yaml
{{ if PIPELINE }}
  # Do something
{{ else if OTHER PIPELINE }}
  # Do something else
{{ else }}
  # Default case
{{ end }}
```

A pipeline is evaluated as false if the value is:

- a boolean false
- a numeric zero
- an empty string
- a nil (empty or null)
- an empty collection (map, slice, tuple, dict, array)

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
data:
  myvalue: "Hello World"
  drink: {{ .Values.favorite.drink | default "tea" | quote }}
  food: {{ .Values.favorite.food | upper | quote }}
  {{- if eq .Values.favorite.drink "coffee" }}
  mug: "true"
  {{- end }}
```

## cheat sheet

```bash
# list installed charts
helm ls -A

# read chart
helm show all|chart|readme|values prometheus-community/kube-state-metrics

# repo
helm repo add any-name https://prometheus-community.github.io/helm-charts
helm repo list
helm repo update
helm repo remove any-name

# install 
helm install kube-state-metrics prometheus-community/kube-state-metrics
## installing with custom configuration
helm install -f wordpress.yaml kube-state-metrics prometheus-community/kube-state-metrics

# upgrade
helm upgrade kube-state-metrics prometheus-community/kube-state-metrics --version 5.10.0 -n metric

# create
helm create foo
# foo/
# ├── .helmignore   # Contains patterns to ignore when packaging Helm charts.
# ├── Chart.yaml    # Information about your chart
# ├── values.yaml   # The default values for your templates
# ├── charts/       # Charts that this chart depends on
# └── templates/    # The template files
#     └── tests/    # The test files


# To view helm chart
helm template chart-name

# view history of chart changes
helm history chart-name

# rollback to most recent version of chart
helm rollback chart-name
# rollback to specific revision version
helm rollback chart-name <revision-number>

```
