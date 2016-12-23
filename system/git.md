# Git User Guide

## Install&Config
yum install git
vim /etc/gitconfig

```conf
    [user]
        email = alvinyeats@gmail.com
        name = alvin
    [core]
        autocrlf = false
```

## tag使用方法

- 创建附注类标签：git tag -a <tagname> -m 'my version'
- 推送至远程分支：git push origin <tagname> 或 git push origin --tags
- 删除本地tag: git tag -d <tagname>
- 删除远程分支tag：git push origin -d tag <tagname>

---