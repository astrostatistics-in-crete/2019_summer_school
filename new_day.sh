#!/bin/csh
clear
echo "Hello astrostatistics student..."
echo
echo ">>>>  ACTIVATING PYTHON 3.6  <<<<"
conda activate py36
echo ">>>>  DOWNLOADING ASTROSTAT19 DATA  <<<<"
python get_data.py
echo ">>>>  EXECUTING JUPYTER NOTEBOOK  <<<<"
jp
