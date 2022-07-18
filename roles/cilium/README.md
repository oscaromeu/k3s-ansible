Ansible Role Cilium
=========

[![CI](https://github.com/oscaromeu/ansible-role-cilium/actions/workflows/ci.yml/badge.svg)](https://github.com/oscaromeu/ansible-role-cilium/actions/workflows/ci.yml)

This role installs cilium cli

Requirements
------------

NA

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`)

```yml
uninstall_tools: true
```

By default the platform is linux and the architecture is arm64 (`os_arch: arm64`) . These variables are checked and configured at runtime by the role so its not necessary to adjust them.

```yml
cilium_version: '0.11.11'
```

Using these variables the binaries can be upgraded or downgraded.

```yml
cilium_bin_path: /usr/local/bin/helm
```

The location where the cilium binary will be installed.

Dependencies
------------

In order to run molecule test the following has to meet

```
molecule 4.0.0 using python 3.10
ansible:2.12.2
docker:1.1.0 from molecule_docker requiring collections: community.docker>=1.9.1
vagrant:1.0.0 from molecule_vagrant
```

Example Playbook
----------------


```yml
    - hosts: all
      roles:
         - { role: oscaromeu.ansible_role_cilium }
```

Execute test with molecule
---------------------------------------------------

 __NOTE:__ Set the following variable if there is no colored output when executing molecule

```
export ANSIBLE_FORCE_COLOR=1
```


## Spin up test environment
```
molecule create -s default
```

## Execute test against test environment
```
molecule converge -s default -- 
```

Any argument after passed after the `--` will be parsed by ansible e.g execute ansible with verbose output 

```
molecule converge -s default -- -vvv
```

License
-------

Apache 2.0

Author Information
------------------

This role was created by Oscar Romeu
