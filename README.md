TSM-CLIENT
=========

The role installs and configures tsm client for RHEL and CentOS servers.


Requirements
------------

The role interacts with TSM server.

Role Variables
--------------
The main variables:
- `tsm_server_name`: the TSM server name.
- `tsm_server_address`: TSM server fqdn/hostname or ip.
- `tsm_server_password`: The tsm server password
- `tsm_server_admin_username`: The TSM admin username
- `tsm_policy_name`: The policy name.
- `tsm_policy_domain`: The policy domain.

Some defaults (probably not requiring tampering)
- `sm_sys_path`: /opt/tivoli/tsm/client/ba/bin/dsm.sys
- `dsm_opt_path:`: /opt/tivoli/tsm/client/ba/bin/dsm.opt
- `inclexcl_path`: /opt/tivoli/tsm/client/ba/bin/InclExcl
- `inclexcl_local_path`: /opt/tivoli/tsm/client/ba/bin/InclExcl.local
- `tsm_pwd_path`: /etc/adsm/TSM.PWD


Dependencies
------------

Currently there are no role dependencies.


Example Playbook
----------------

```yaml
- hosts: example.com
  become: true
  vars:
      tsm_server_password: TSM_SERVER_PASSWORD
      tsm_server_address: tsm.server.fqnd.com
      tsm_server_name: SERVER_NAME
      tsm_server_admin_username: ADMIN_USERNAME
      tsm_policy_name: DAILY_INCREMENTAL_LINUX
      tsm_policy_domain: TSM_POLICY_DOMAIN
  roles:
    - tsm-client

```

License
-------

GPLv2

Author Information
------------------

Michael Angelos Simos

[www.asimos.tk](https://www.asimos.tk)
