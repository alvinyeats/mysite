# 配置文档

- System: CentOS 7.0
- Web framework: Django 1.10.4
- Basic Language: Python 3.4.5
- SQL: PostgreSQL 9.2.18
- Reverse Proxy: Nginx
- WSGI HTTP Server: gunicorn

---

## CentOS 7.0 基础环境配置

### 更换yum镜像

cd /etc/yum.repos.d/

yum -y install epel-release
mv epel.repo epel.repo.back
wget -O epel.repo  http://mirrors.aliyun.com/repo/epel-7.repo

mv CentOS-Base.repo CentOS-Base.repo.back
wget -O CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

yum clean all
yum makecache

### vim安装、简配

yum install vim
cd ~
vim .vimrc

```vim
    syntax on
    set ts=4
    set softtabstop=4
    set expandtab
    set nu
```

### 安装python34及pip

yum install python34

cd ~
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py

#### pip设置

vim /etc/pip.conf

```conf
    [global]
        index-url=http://mirrors.aliyun.com/pypi/simple/
    [install]
        trusted-host=mirrors.aliyun.com
    [list]
        format=columns
```

### 安装PostgreSQL及Nginx

```shell
    yum install -y python34-devel postgresql-server postgresql-devel postgresql-contrib gcc nginx
```

### install VBoxGusudestAdditions

```shell
    yum update kernel
    yum install kernel-devel bzip2 gcc-c++
    poweroff

    （添加C:\Program Files\Oracle\VirtualBox\VBoxGuestAdditions.iso）

    export MAKE='/usr/bin/gmake -i'
    mkdir /mnt/cdrom
    mount -t auto /dev/cdrom /mnt/cdrom
    /mnt/cdrom/VBoxLinuxAdditions.run
```

## 数据库初始化

```shell
sudo postgresql-setup initdb
sudo systemctl start postgresql

vim /var/lib/pgsql/data/pg_hba.conf
```
```conf
    local   all             all                                     peer
    host    all             all             127.0.0.1/32            md5
    host    all             all             ::1/128                 md5
```
```shell
    sudo systemctl restart postgresql
    sudo systemctl enable postgresql
    sudo su - postgres
    psql
    CREATE USER dbuser WITH PASSWORD 'password';
    CREATE DATABASE exampledb OWNER dbuser;
    GRANT ALL PRIVILEGES ON DATABASE exampledb to dbuser;
    \q
```

## 项目配置

### 创建www用户并设置共享

groupadd -g 83 www
useradd -u 83 -g www www
mkdir -p /data/www/mysite
chown -R www:www /data/www
mkdir -p /data/static
chown -R www:www /data

（挂载项目->固定分配）

vim /etc/rc.local

```conf
    mount -t vboxsf -o uid=83,gid=83 mysite /data/www/mysite
```
chmod +x /etc/rc.d/rc.local
/etc/rc.local

### 配置python虚拟环境

sudo pip install virtualenv
cd /data/www
virtualenv mysiteenv
source mysiteenv/bin/activate
cd mysite
pip install -r requirements.txt

### 运行项目

cd /data/www/mysite
./manage.py migrate
./manage.py makemigrations
./manage.py collectstatic


## gunicorn

mkdir /var/log/gunicorn
chown www:www /var/log/gunicorn

vim /etc/systemd/system/gunicorn.service

```conf
    [Unit]
    Description=gunicorn daemon
    After=network.target

    [Service]
    User=www
    Group=www
    WorkingDirectory=/data/www/mysite
    ExecStart=/data/www/mysiteenv/bin/gunicorn --workers 3 --max-requests 10 --user www --group www --log-level debug --error-logfile /var/log/gunicorn/error.log --bind unix:/data/www/mysite.sock blog.wsgi:application

    [Install]
    WantedBy=multi-user.target
```
chmod 755 /etc/systemd/system/gunicorn.service

systemctl start gunicorn
systemctl stop firewalld
systemctl disable firewalld
systemctl enable gunicorn


## nginx

``` shell
    vim /etc/nginx/nginx.conf

    修改用户
    修改server配置

    systemctl start nginx
    systemctl enable nginx

```

## Git User Guide

### Install&Config
yum install git
vim /etc/gitconfig

```conf
    [user]
        email = alvinyeats@gmail.com
        name = alvin
    [core]
        autocrlf = false
```

### tag使用方法

- 创建附注类标签：git tag -a <tagname> -m 'my version'
- 推送至远程分支：git push origin <tagname> 或 git push origin --tags
- 删除本地tag: git tag -d <tagname>
- 删除远程分支tag：git push origin -d tag <tagname>

---

### 数据的导入导出

命令操作：
数据的导出：pg_dump -U postgres(用户名)  (-t 表名)  数据库名(缺省时同用户名)  > c:\fulldb.sql
数据的导入：psql -U postgres(用户名)  数据库名(缺省时同用户名) < C:\fulldb.sql