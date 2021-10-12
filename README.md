# ![Raspberry Pi](docs/img/logo_raspberry-pi.svg) k3s playground 

## TODO

This project is derived from [k3s-ansible](https://github.com/k3s-io/k3s-ansible) and the goal is to easily spin up and configure k3s cluster with all the needed tools via Ansible. 
 
- [X] Debian
- [X] Ubuntu
- [ ] Arch Linux

on processor architecture:

- [X] arm64

## System requirements

+ Deployment environment must have Ansible 2.4.0+
+ Master and nodes must have passwordless SSH access

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

## Remove

To remove the provisioned infrastructure use the following command:

```bash
ansible-playbook reset.yml -i inventory/my-cluster/hosts.ini
```

## Status and Backlog
- [ ] Update README (WIP)
- [ ] Support installation of Flux V2 configured via config file (WIP)
- [ ] Automatically Deploying Manifest and Helm Charts (WIP)
- [ ] Review roles (WIP)
- [ ] Deploy the default K8s dashboard (WIP) 
- [ ] Support to deploy rancher-monitoring
- [ ] Support configure K3s with a configuration file avaible from v1.19.1+k3s1
- [ ] Support via configuration file:
  - [ ] Configure K3s with a configuration file avaible from v1.19.1+k3s1
  - [ ] Deploy High Availability with External DB
  - [ ] Deploy High Availability with Embedded DB
  - [ ] Support different cluster datastore options
  - [ ] Support Private registry configuration
- [ ] Support to deploy a handcrafted monitoring solution for the k3s cluster.
- [ ] Customize Traefik via HelmChartConfig manifest
- [ ] Install Rancher Helm Chart
- [ ] Support Arch based linux distros running on Raspberry Pi


## Author

oscaromeu (https://github.com/oscaromeu)

## License

This software is released under the Apache License, see LICENSE.
