# -*- coding: utf-8 -*-
import os
import json
from pprint import pprint

path = "/home/david/Área de Trabalho/2019_08_22-15_45_48"
files = os.listdir(path)

accelerations = None
can_frames = None
frames = None
locations = None
pressures = None
rotations = None

for file in files:
    if(".json" in file):
        #print(file[:-4])
        if(file[:-5] == "can_frames"):
            with open(path + "/" + file) as data_file:
                can_frames = json.load(data_file)
            #pprint(data)
        if(file[:-5] == "acc"):
            with open(path + "/" + file) as data_file:
                can_frames = json.load(data_file)
        if(file[:-5] == "accelerations"):
            with open(path + "/" + file) as data_file:
                can_frames = json.load(data_file)
        if(file[:-5] == "frames"):
            with open(path + "/" + file) as data_file:
                can_frames = json.load(data_file)
        if(file[:-5] == "locations"):
            with open(path + "/" + file) as data_file:
                can_frames = json.load(data_file)
        if(file[:-5] == "pressures"):
            with open(path + "/" + file) as data_file:
                can_frames = json.load(data_file)
        if(file[:-5] == "rotations"):
            with open(path + "/" + file) as data_file:
                rotations = json.load(data_file)

for axis in rotations["rotations"]:
    print(axis)
