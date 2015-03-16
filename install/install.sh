#!/bin/bash

echo  "Creating $HOME/bin/IC_lunch folder..."
mkdir -p $HOME/bin/IC_lunch
cp -R $( dirname $( dirname $( readlink -f $0 ) ) )/* $HOME/bin/IC_lunch/

if [ -f $HOME/bin/IC_lunch/requirements.txt  ]
then
    echo -e "Installing requirements...\n"
    pip install --user -r $HOME/bin/IC_lunch/requirements.txt
fi

echo -e "Add the following to your .zshrc or .bashrc file (or whatever analogue for your own shell)\n"
echo -e "########################################################\n"
cat $( dirname  $( dirname $( readlink -f $0 ) ) )/.add_path_example.txt
echo -e "\n########################################################\n\n"


