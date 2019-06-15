import os
import requests

parent = "http://astro.physics.uoc.gr/Conferences/Astrostatistics_School_Crete_2019/data/"
datafiles_name = "datafiles"

# get datafile list
request = requests.get(parent + datafiles_name)
datafiles_content = request.text

filepaths = datafiles_content.split()

# get all files
for filepath in filepaths:
    if not filepath.startswith("./"):
        raise Exception("Unexpected entry of datafiles.")

    filepath = filepath[2:]
    if filepath == datafiles_name:
        continue

    folder, filename = os.path.split(filepath)
    local_filename = os.path.join(folder, "data", filename)
    #print(folder, filename, local_filename)

    url = parent + filepath

    wget_cmd = "wget -O {} {}".format(local_filename, url)
    os.system(wget_cmd)
