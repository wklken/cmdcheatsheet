A quick cheatsheet command line tool in shell
===========================================

CSData means CheatSheetData

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



