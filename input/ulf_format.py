# -*- coding: utf-8 -*-

import json

with open('C:/Users/rgibs/Downloads/ulf-1.0.json') as f: 
    data = json.load(f)
    with open('C:/Users/rgibs/Downloads/ulf_dataset_all.txt', 'w') as output:
        #loop through all objects in json
        for i in data:
            output.write(i[2] + '\n') #ULF
            output.write(i[1] + '\n') #English
            output.write('<|endoftext|>\n')


