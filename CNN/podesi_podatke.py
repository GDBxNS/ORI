from shutil import copyfile
import os

import pandas as pd

CSV_DIR = "chest_xray_data_set/metadata/chest_xray_metadata.csv"
DATA_DIR = "chest_xray_data_set"
NORMAL_DIR = "Dataset/Training/Normal"
VIRUS_DIR = "Dataset/Training/Virus"
BACTERIA_DIR = "Dataset/Training/Bacteria"

podaci = pd.read_csv(CSV_DIR, usecols=['Label', 'X_ray_image_name', 'Label_1_Virus_category'])

for index in range(len(podaci["Label"])):

    if(podaci["Label"][index] == "Normal"):
        copyfile(os.path.join(DATA_DIR, podaci["X_ray_image_name"][index]),
                 os.path.join(NORMAL_DIR, podaci["X_ray_image_name"][index]))

    elif(podaci["Label"][index] == "Pnemonia"):
        if(podaci["Label_1_Virus_category"][index] == 'bacteria'):
            copyfile(os.path.join(DATA_DIR, podaci["X_ray_image_name"][index]),
                     os.path.join(BACTERIA_DIR, podaci["X_ray_image_name"][index]))

        elif(podaci["Label_1_Virus_category"][index]=='Virus'):
            copyfile(os.path.join(DATA_DIR, podaci["X_ray_image_name"][index]),
                     os.path.join(VIRUS_DIR, podaci["X_ray_image_name"][index]))

