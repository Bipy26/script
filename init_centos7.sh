#!/bin/bash

# 适用于CentOS7

# 更改dns
echo "nameserver 223.5.5.5" >/etc/resolv.conf

# 关闭 SeLinux | 阿里云镜像默认已配置
setenforce 0
sed -i "s/SELINUX=enforcing/SELINUX=disabled/g" /etc/selinux/config

# 关闭 防火墙 | 阿里云镜像默认已配置
systemctl stop firewalld
systemctl disable firewalld

# 开放端口
# firewall-cmd --zone=public --add-port=80/tcp --permanent
# firewall-cmd --zone=public --add-port=443/tcp --permanent
# firewall-cmd --reload
# firewall-cmd --zone=public --list-all

# 更换国内源
cp /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
yum -y install wget
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
yum list | grep epel-release
yum install -y epel-release
wget -O /etc/yum.repos.d/epel-7.repo http://mirrors.aliyun.com/repo/epel-7.repo
yum clean all
yum makecache

# 安装常用软件
yum install -y vim bash-completion bash-completion-extras zip unzip make gcc gcc-c++ git wget lsof net-tools psmisc mtr iotop iftop bind-utils tree dos2unix nmap htop
yum -y update

# 修改时区
# timedatectl开启的ntp服务取决于chronyd或者ntpd哪个被安装
timedatectl set-timezone Asia/Shanghai
timedatectl status