#! /bin/env bash

apt install python3-pip python3.11-venv -y

#virtual env
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt

python3 MOXhemes.py

cd .. && rm -rf MOX_Themes && cd ~

deactivate
