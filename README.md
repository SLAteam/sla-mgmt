# sla-mgmt
Web SLA management application based on Django

## Prerequisites
Python 3.6

## How to run
Recommended is to run it at virtualenv:

```
python3 -m venv sla-mgmt-venv
source sla-mgmt-venv/bin/activate
```

Required steps:
```
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

To run parser, add sla to your PATH and export SLA_ROOT:
```
export SLA_ROOT=<path_to_project>
export PYTHONPATH=$PYTHONPATH:$SLA_ROOT/sla:$SLA_ROOT/sla_app
```

Then:
```
python sla/parsers/parser_for_3rd_report.py report3_m2m_network_for_customer_b.csv 0
```
