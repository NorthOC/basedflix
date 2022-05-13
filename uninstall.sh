#!/bin/bash

echo "Removing symlink"
sudo rm /usr/local/bin/basedflix

read -p "Delete webtorrent-cli? (1 = YES, or press Enter for NO): " delvar

if [ "$delvar" == "1" ]; then
    sudo npm uninstall -g webtorrent-cli
fi

echo "The program was uninstalled succesfully!"
echo "Have a good one matey!"
echo
echo "                           ~NorthOC"
echo