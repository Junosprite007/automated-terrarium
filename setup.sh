#!/bin/bash

############### Setting up Raspberry Pi automation from within the Pi ###############

# run from remote machine
# cat automation.py | ssh pibay2 python -

sudo apt -y update && sudo apt -y upgrade
sudo apt -y install git

cd ~/

mkdir apps
cd apps

# clone repo
git clone https://github.com/Junosprite007/automated-terrarium.git

cd automated-terrarium
