import os
import requests

parent = "http://astro.physics.uoc.gr/Conferences/Astrostatistics_School_Crete_2019/data/"
datafiles_name = "datafiles"
setupdata_name = "setup_data"

for filepath in requests.get(parent + datafiles_name).text.split():
    if not filepath.startswith("./"):
        raise Exception("Unexpected entry of datafiles.")
    filepath = filepath[2:]
    if filepath != datafiles_name and filepath != setupdata_name:
        folder, filename = os.path.split(filepath)
        local_folder = os.path.join(folder, "data")
        local_filename = os.path.join(local_folder, filename)
        os.system("mkdir {}".format(local_folder))
        os.system("wget -O {} {}".format(local_filename, parent + filepath))
