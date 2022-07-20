# Ansible Role Flux

[![CI](https://github.com/oscaromeu/ansible-role-k8s-tools/actions/workflows/ci.yml/badge.svg)](https://github.com/oscaromeu/ansible-role-k8s-tools/actions/workflows/ci.yml)

This role installs [Flux V2](https://fluxcd.io/docs/cmd/) cli

## Requirements

```
molecule 4.0.0 using python 3.10
ansible:2.12.2
docker:1.1.0 from molecule_docker requiring collections: community.docker>=1.9.1
vagrant:1.0.0 from molecule_vagrant
```

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yml
uninstall: false
```

If set to true it will only remove the installed cli. 

```yml
flux_platform: linux
```

By default the platform is `linux`. 

```yml
helm_version: 'v3.2.1'
```

Using these variables the binaries can be upgraded or downgraded. 

```yml
flux_bin_path: /usr/local/bin/flux
```

The location where the flux binary will be installed.

## Dependencies

None.

## Examples

### Example Playbook

```yaml
    - hosts: all
      roles:
        - role: oscaromeu.flux
```

### Execute example playbook locally

```
ansible-playbook --connection=local --inventory 127.0.0.1, playbook.yml --ask-become-pass
```

### Execute test with molecule

#### Run test sequence commands

Run molecule to create an instance with:

```
$ molecule create -s default
```

Test the role against our instances with:

```
$ molecule converge -s default --
```

Verify that the role pass the test:

```
$ molecule verify
```

Finally, we can destroy the instances with:

```
$ molecule destroy
```

#### Run a full test sequence

The full lifecycle sequence can be invoked with:

```
$ molecule test
```

__Note:__ Getting colorized output from molecule and Ansible

```
export ANSIBLE_FORCE_COLOR=1
```

## License

MIT / BSD

## Author Information

This role was created by Oscar Romeu.
 

