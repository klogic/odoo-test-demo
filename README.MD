# Odoo Test Demo

## About This
This module is demo of testing in odoo.

## command
```python

# view odoo runing & scritp command on ubunt
$ ps aux | grep odoo-server

# create new module
# command: python /usr/bin/odoo scaffold <module_name>
python /usr/bin/odoo scaffold test_module

# runing test
# command: python /usr/bin/odoo -u <module_name> -i <module_name> --test-enable --config <config_server_file> --logfile <logfile_location>
python /usr/bin/odoo -u automate_test -i automate_test --test-enable --config /etc/odoo/odoo.conf  --logfile /var/log/odoo/odoo-server.log

```

## Debug
1. run test command
2. in another tab. open log file for watch test result.

