# 安装anaconda

[TOC]

##安装anaconda

系统的环境为：**Ubuntu18.04+cuda10.1**

在anaconda [官网](<<https://www.anaconda.com/distribution/>>)找到相应的配置参数，下载相应的版本

![image-20190402160924537](/Users/ouyang/Library/Application Support/typora-user-images/image-20190402160924537.png)



下载完成后，运行一下命令安装：

```
bash Anaconda3-2018.12-Linux-x86_64.sh
```

然后激活环境变量即可：

```
source /root/anaconda3/etc/profile.d/conda.sh
2019.5.28
source /home/***/.bashrc
```

运行

```
conda
usage: conda [-h] [-V] command ...

conda is a tool for managing and deploying applications, environments and packages.

Options:

positional arguments:
  command
    clean        Remove unused packages and caches.
    config       Modify configuration values in .condarc. This is modeled
                 after the git config command. Writes to the user .condarc
                 file (/root/.condarc) by default.
    create       Create a new conda environment from a list of specified
                 packages.
    help         Displays a list of available conda commands and their help
                 strings.
    info         Display information about current conda install.
    install      Installs a list of packages into a specified conda
                 environment.

```

安装成功



## conda命令的使用

###**创建环境**

创建python2的环境

conda create -n py3 python=3

### 进入环境

conda activate py3

### 离开环境

conda deactivate 
