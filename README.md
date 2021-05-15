# ![New Button](docs/img/logo_raspberry-pi.svg) k3s Ansible Deploy Monitoring Playground

**TODO**

This work is derived from [k3s-ansible](https://github.com/k3s-io/k3s-ansible). The goal is to spin up a monitoring infrastructure running in a Kubernetes cluster. The project supports the following machines running: 

- [X] Debian

on processor architecture:

- [X] arm64
- [X] armhf

## System requirements

Deployment environment must have Ansible 2.4.0+
Master and nodes must have passwordless SSH access

## Usage

### Deploy

First create a new directory based on the `sample` directory within the `inventory` directory:

```bash
cp -R inventory/sample inventory/my-cluster
```

Second, edit `inventory/my-cluster/hosts.ini` to match the system information gathered above. For example:

```bash
[master]
192.16.35.12

[node]
192.16.35.[10:11]

[k3s_cluster:children]
master
node
```

If needed, you can also edit `inventory/my-cluster/group_vars/all.yml` to match your environment.

Start provisioning of the cluster using the following command:

```bash
ansible-playbook site.yml -i inventory/my-cluster/hosts.ini
```

### Kubeconfig

To get access to your **Kubernetes** cluster just

```bash
scp debian@master_ip:~/.kube/config ~/.kube/config
```


## Remove

To remove the provisioned infrastructure use the following command:

```bash
ansible-playbook reset.yml -i inventory/my-cluster/hosts.ini
```

## TODO
- [ ] Deploy the following components via helm:
    - [ ] Prometheus
    - [ ] Grafana
    - [ ] Influxdb
    - [ ] Telegraf
    - [ ] Redis + Logstash + Elasticsearch Cluster
    - [ ] Elastalert
    - [ ] ArgoCD
- [ ] ...



## Author

oscaromeu (https://github.com/oscaromeu)

## License

This software is released under the MIT License, see LICENSE.
