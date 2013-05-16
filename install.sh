#!/bin/bash
#install the cheetsheet to $HOME/bin

#cheatsheet data
CHEATSHEETDATA='CSData'
#cheatsheet.py
CHEATSHEETFILE='cheatsheet.py'

#the shortcut of command, you can set your own
SHORT_CMD='cs'
if [ -n "$1" ]
then
    SHORT_CMD="$1"
fi

BASEDIR=$(dirname $0)
cd $BASEDIR 
CURRENT_DIR=`pwd`

if [ ! -d $HOME/bin ]
then
    mkdir -p $HOME/bin
fi

if [ -L $HOME/bin/$SHORT_CMD ]
then
    unlink $HOME/bin/$SHORT_CMD
fi
ln -s  $CURRENT_DIR/$CHEATSHEETFILE $HOME/bin/$SHORT_CMD

if [ -L $HOME/bin/$CHEATSHEETDATA ]
then
    unlink $HOME/bin/$CHEATSHEETDATA
fi
ln -s $CURRENT_DIR/$CHEATSHEETDATA $HOME/bin/$CHEATSHEETDATA

\chmod 700 $CURRENT_DIR/cheatsheet.py 
\chmod 700 $CURRENT_DIR/$CHEATSHEETDATA
