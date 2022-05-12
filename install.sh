#!/bin/bash

# to stop script at errors
set -eu

echo "Creating virtual python environment (venv)..."
python3 -m venv venv

echo "Installing packages to virtual environment from requirements.txt..."
source ./venv/bin/activate
pip install -r requirements.txt
deactivate

# directory of the repo folder on your computer
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo "setting the location of python files..."
echo "adding location to basedflix.sh as: $SCRIPT_DIR"

cat << EOF > $SCRIPT_DIR/basedflix.sh
#!/bin/bash
cd $SCRIPT_DIR
source ./venv/bin/activate
python3 main.py
EOF

#feel free to modify these parts below
echo "basedflix.sh file updated"
echo "checking or creating ~/.local/bin"

mkdir -p ~/.local/bin

echo "adding (export PATH= ~/.local/bin) to .bashrc"

# remove or set a specific path you want
cat << EOF >> ~/.bashrc
export PATH="\$PATH:$HOME/.local/bin"
EOF

# set whatever directory you want to copy the basedflix file to
echo "copying script basedflix.sh to ~/.local/bin"
cp $SCRIPT_DIR/basedflix.sh ~/.local/bin/basedflix

source ~/.bashrc
echo "All done! Now you can type basedflix to start the program!"