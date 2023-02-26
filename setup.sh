#!/bin/bash

############### Setting up Raspberry Pi automation from within the Pi ###############

sudo apt -y update && sudo apt -y upgrade
sudo apt -y install git

cd ~/

mkdir apps
cd apps

# Quietly tranfer folder from other computer to the raspi, or clone from remote repo.
# scp -rq ../automated-terrarium pibay2:~/apps/

cd automated-terrarium