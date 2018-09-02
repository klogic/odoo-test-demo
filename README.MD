# Odoo Test Demo

## About This
This module is demo of testing in odoo.

## Command

**View odoo runing & scritp command on ubuntu**
```bash
$ ps aux | grep odoo-server
```

**Create new module Command:** python /usr/bin/odoo scaffold <module_name>
```bash
$ python /usr/bin/odoo scaffold test_module
```

**Runing test command:** python /usr/bin/odoo -u <module_name> -i <module_name> --test-enable --config <config_server_file> --logfile <logfile_location>
```bash
$ python /usr/bin/odoo -u automate_test -i automate_test --test-enable --config /etc/odoo/odoo.conf  --logfile /var/log/odoo/odoo-server.log
```


## Debug
1. run test command
2. in another tab. open log file for watch test result.

