# Welcome to Mysite Project

- System: CentOS 7.0
- Web framework: Django 1.10.4
- Main Language: Python 3.4.5
- SQL: PostgreSQL 9.2.18
- Reverse Proxy: Nginx 1.10.2
- WSGI HTTP Server: gunicorn 19.6.0


## User Guide

### Get Source Code

``` shell
    git clone git@github.com:alvinyeats/mysite.git
```

### Virtualenv Config

```shell
    sudo yum install python34
    virtualenv your_python_env -p python3
    source your_python_env/bin/activate

    cd path_to/mysite
    pip install -r requirements.txt
```
