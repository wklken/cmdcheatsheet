A quick cheatsheet command line tool in shell
===========================================

CSData means CheatSheetData

##Install

git clone 

use default short cmd : cs

    sh -x install.sh

you can define your own short cmd: mycs

    sh -x install.sh mycs

##Test
if install default:

    cs test
    
if you defined your own short cmd: mycs

    mycs test


##Edit
Edit your own cheatsheet in dir:

1.create one type of cheatsheet file your need

  ext is .kv

    touch vim.kv shell.kv

2.edit the content
  
  the format is yaml[one kind of config file]

    newkey: |
        value1
        value2

3.then test:

    cheatsheet newkey



