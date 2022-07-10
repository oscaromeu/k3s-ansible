# ![Raspberry Pi](documentation/img/logo_raspberry-pi.svg) k3s ansible 


This project starts from [k3s-ansible](https://github.com/k3s-io/k3s-ansible) and adds some features and changes. The goal is to easily spin up and configure k3s cluster with all the needed tools via Ansible. 

## Prerequisites 

Deployment environment must have Ansible > 2.4.0+. Master and worker nodes its desired that have passwordless SSH access. This role has been tested againts the following distributions:

- [X] Debian

on processor architecture:

- [X] arm64
- [X] x86

## TODO

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

## Author

oscaromeu (https://github.com/oscaromeu)

## Original Work 

https://github.com/itwars

https://github.com/k3s-io/k3s-ansible

## License

This software is released under the Apache License, see LICENSE.
