#!/bin/bash

echo  "Creating $HOME/bin/IC_lunch folder..."
mkdir -p $HOME/bin/IC_lunch
cp -R $( dirname $( dirname $( readlink -f $0 ) ) )/* $HOME/bin/IC_lunch/


echo -e "Installing requirements...\n"
pip install --user beautifulsoup4

cp $( dirname $( readlink -f $0 ) )/path_add $HOME/.path_add

if [ -f $HOME/.bashrc ]
then
    echo 'source $HOME/.path_add' >> $HOME/.bashrc
fi

if [ -f $HOME/.zshrc ]
then
    echo 'source $HOME/.path_add' >> $HOME/.zshrc
fi

if [ -f $HOME/.cshrc  ]
then
    echo 'source $HOME/.path_add' >> $HOME/.cshrc
fi
