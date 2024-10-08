# rate-limits-exporter

![Version: 2.0.1](https://img.shields.io/badge/Version-2.0.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: v2.0.0](https://img.shields.io/badge/AppVersion-v2.0.0-informational?style=flat-square)

Docker Hub rate limits exporter for Prometheus

**Homepage:** <https://github.com/bissquit/rate-limits-exporter.git>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| Egor Vasilyev |  | <https://github.com/bissquit> |

## Source Code

* <https://github.com/bissquit/rate-limits-exporter.git>
* <https://github.com/bissquit/helm-rate-limits-exporter.git>

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` |  |
| app.dockerhub_password | string | `""` | DockerHub password. As secure alternative use [access token](https://docs.docker.com/security/for-developers/access-tokens/) instead |
| app.dockerhub_username | string | `""` | DockerHub username |
| app.log_level | string | `"DEBUG"` | Default log level |
| app.loop_time | int | `60` | Default time range in seconds to perform rate limits checks |
| app.port | int | `8080` | Port to be listened by application in POD. This option doesn't change Service port (use service.port). |
| app.put_source_ip | bool | `false` | Source ip address from headers will be inserted into labels. Be careful to use this option because many different ip addressess in the label set will produce a lot of new time series in Prometheus TSDB. Read **CAUTION** in official article [METRIC AND LABEL NAMING](https://prometheus.io/docs/practices/naming/) |
| fullnameOverride | string | `""` |  |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.repository | string | `"bissquit/rate-limits-exporter"` |  |
| image.tag | string | `""` |  |
| imagePullSecrets | list | `[]` |  |
| livenessProbe.httpGet.path | string | `"/healthz"` |  |
| livenessProbe.httpGet.port | int | `8080` |  |
| livenessProbe.initialDelaySeconds | int | `30` |  |
| livenessProbe.periodSeconds | int | `30` |  |
| nameOverride | string | `""` |  |
| nodeSelector | object | `{}` |  |
| podAnnotations | object | `{}` |  |
| podLabels | object | `{}` |  |
| podSecurityContext | object | `{}` |  |
| readinessProbe.httpGet.path | string | `"/metrics"` |  |
| readinessProbe.httpGet.port | int | `8080` |  |
| readinessProbe.initialDelaySeconds | int | `30` |  |
| readinessProbe.periodSeconds | int | `30` |  |
| replicaCount | int | `1` |  |
| resources.limits.cpu | string | `"100m"` |  |
| resources.limits.ephemeral-storage | string | `"100Mi"` |  |
| resources.limits.memory | string | `"128Mi"` |  |
| resources.requests.cpu | string | `"50m"` |  |
| resources.requests.ephemeral-storage | string | `"100Mi"` |  |
| resources.requests.memory | string | `"64Mi"` |  |
| securityContext.readOnlyRootFilesystem | bool | `true` |  |
| securityContext.runAsGroup | int | `65534` |  |
| securityContext.runAsNonRoot | bool | `true` |  |
| securityContext.runAsUser | int | `65534` |  |
| service.port | int | `80` |  |
| service.type | string | `"ClusterIP"` |  |
| serviceAccount.annotations | object | `{}` |  |
| serviceAccount.automount | bool | `true` |  |
| serviceAccount.create | bool | `true` |  |
| serviceAccount.name | string | `""` |  |
| tolerations | list | `[]` |  |
| volumeMounts | list | `[]` |  |
| volumes | list | `[]` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)
