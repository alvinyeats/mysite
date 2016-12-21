
## virtualbox 共享文件设置

因为centos7.0的启动问题， 将共享文件挂载写入fstab会出问题，采用手动挂载的方式：

编辑 '/etc/rc.local'

加入：'mount -t vboxsf -o uid=83,gid=83 mysite /data/www/mysite'

然后加入可执行权限：'chmod +x /etc/rc.d/rc.local'

这样每次开机系统读取rc.local时便会自动挂载共享目录了
