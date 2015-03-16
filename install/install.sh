#!/bin/bash

echo  "Creating $HOME/bin/IC_lunch folder..."
mkdir -p $HOME/bin/IC_lunch
cp -R $( dirname $( dirname $( readlink -f $0 ) ) )/* $HOME/bin/IC_lunch/

if [ -f $HOME/bin/IC_lunch/requirements.txt  ]
then
    echo -e "Installing requirements...\n"
    pip install --user -r $HOME/bin/IC_lunch/requirements.txt
fi

mv $( dirname $( readlink -f $0 ) )/.add_path_example.txt $HOME/.path_adder

if [ -f $HOME/.bashrc ]
then
    echo 'source $HOME/.path_adder' >> $HOME/.bashrc
fi

if [ -f $HOME/.zshrc ]
then
    echo 'source $HOME/.path_adder' >> $HOME/.zshrc
fi

if [ -f $HOME/.cshrc  ]
then
    echo 'source $HOME/.path_adder' >> $HOME/.cshrc
fi
