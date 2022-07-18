# ![Raspberry Pi](documentation/img/logo_raspberry-pi.svg) k3s ansible 


This project starts from [k3s-ansible](https://github.com/k3s-io/k3s-ansible) and adds some features and changes. The major change is that all the configuration of the master and agent nodes is done via [configuration file](https://rancher.com/docs/k3s/latest/en/installation/install-options/#configuration-file) instead of CLI arguments.

## Prerequisites 

Deployment environment must have Ansible > 2.4.0+. Master and worker nodes its desired that have passwordless SSH access. This role has been tested againts the following distributions:

- [X] Debian/Raspbian
    - Debian 11 bullseye 
- [X] Ubuntu
    - Ubuntu 22.04 LTS (Jammy Jellyfish)

on processor architecture:

- [X] arm64
- [X] x86

## Repository structure

The Git repository contains the following directories

```
├── collections
├── ...
├── inventory
│   ├── ...
|   └── sample
├── roles
│   ├── cilium
│   ├── cni
│   ├── download
│   ├── k3s
│   ├── pip
│   ├── postsetup
│   ├── prereq
│   ├── raspberrypi
|   └── reset
├── ...
├── reset.yml
├── site.yml
└── ansible.cfg
```

## Usage

### Default deployment

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

### Deploy k3s with [Calico](https://projectcalico.docs.tigera.io/getting-started/kubernetes/k3s/multi-node-install)

Create an inventory as explained in the default deployment section. Add the following configuration on `roles/k3s/master/defaults/main.yml`

> Note: If 192.168.0.0/16 is already in use within your network you must select a different pod network CIDR by replacing 192.168.0.0/16 in the above command.

```yml
# Server Configuration
k3s_server:
  write-kubeconfig-mode: "0644"
  # calico configuration
  flannel-backend: 'none'
  disable-network-policy: true
  cluster-cidr: "192.168.0.0/16"
```

and in `roles/cni/defaults/main.yml` select calico as a cni provider

```yml
cni_provider: calico
```

Finally start the provisioning the cluster

```
ansible-playbook site.yml -i inventory/my-cluster/hosts.ini
```

### Deploy k3s with [Cilium](https://cilium.io/)

TODO

## Remove

To remove the provisioned infrastructure use the following command:

```bash
ansible-playbook reset.yml -i inventory/my-cluster/hosts.ini
```

## Author

oscaromeu (https://github.com/oscaromeu)

## Original Work 

https://github.com/itwars

https://github.com/k3s-io/k3s-ansible

## License

This software is released under the Apache License, see LICENSE.
