#!/usr/bin/env bash
## Setup script for siftnlp module

# Ensure you have virtualenv and pip[2.7] installed on your local machine
# sudo apt-get install virtualenv # Ubuntu
# sudo yum install virtualenv     # RHEL/CentOS
# brew install virtualenv         # OSX
# Windows: download installer (?)

virtualenv venv
source ./venv/bin/activate
make init
