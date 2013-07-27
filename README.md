A quick cheatsheet command line tool in shell
===========================================

python实现的命令行小抄速查工具

分分钟安装运行，后续不用老是到手册文档文本记录/历史/google那些地方查，用过一次，感觉记不住，加入到数据文件中，后续一个命令查到

可以在文件中录入key:value形式的命令，然后在命令行通过cs key快速查看

可以记录：
    
    vim插件的快捷键
    shell常用/组合命令(很长很难记住的)
    服务器的host/pwd等等，或者跳转命令
    各类语言特性/快捷键/命令
    等等 
    

CSData means CheatSheetData

### Show

![use_img](https://github.com/wklken/gallery/blob/master/tools/cmdcheatsheet.png?raw=true)

##Install

    git clone git@github.com:wklken/cmdcheatsheet.git
    cd cmdcheatsheet
    

use default short cmd : cs

    sh -x install.sh

you can define your own short cmd: mycs

    sh -x install.sh mycs
    

####important
make sure  $HOME/bin in your envionment variables:

    #check if in
    echo $PATH
    
you can add to $HOME/.bashrc or $HOME/.bash_profile:

    echo 'export PATH=$PATH:$HOME/bin' >> $HOME/.bashrc
    source $HOME/.bashrc
    #check again
    echo $PATH

done, the goto Test

##Test
if install default:

    cs test

if you defined your own short cmd: mycs

    mycs test


The result expect in default like this:

    [ken@Luna: ~/bin] cs test
    [host] test
    root:123456
    ken:result

    [vim] test
    root:123456
    ken:result

    [ken@Luna: ~/bin]

if you got this:

    [ken@~/bin$] cs test
    Traceback (most recent call last):
    File "/home/ken/bin/cs", line 8, in <module>
        import yaml

you need to install yaml for python first:

    sudo pip install pyyaml
    



##Edit
Edit your own cheatsheet in dir:

1.create one type of cheatsheet file your need

  ext is .kv

    cd CSData
    vim shell.kv

2.edit the content
  
  the content format is yaml [one kind of config file]

    newkey: |
        value1
        value2

3.then test:

    cheatsheet newkey



