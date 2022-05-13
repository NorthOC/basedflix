#!/bin/bash

# to stop script at errors
set -eu

if [ $(which apt-get) ]; then
  echo "installing dependencies for Ubuntu..."
  sudo apt-get -y install python3 python3-dev python3-pip npm
  sudo npm install webtorrent-cli -g
  sudo pip3 install virtualenv
 
else
  echo "*** You'll need to install Ubuntu or get a working venv for python yourself ***"
fi

echo "Creating virtual python environment (venv)..."
virtualenv venv

echo "Installing packages to virtual environment from requirements.txt..."
source ./venv/bin/activate
pip install --upgrade pip
pip install --upgrade -r requirements.txt

echo "making systemwide symlink in /usr/local/bin"
sudo ln -sf $(pwd)/basedflix /usr/local/bin/basedflix


echo "All done! Now you can type basedflix to start the program!"
echo "Check out README for more info on supported players"
echo
echo "                                    ~NorthOC"
echo