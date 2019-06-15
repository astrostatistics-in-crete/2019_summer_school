#!/bin/bash
clear
echo "Hello astrostatistics student..."

echo ">> activating Python 3.6"
conda activate py36

echo ">> downloading data"
py36 get_data.py

echo ">> executring jupyter notebook"
jp
