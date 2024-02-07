'''
CIS 210 proj 6
Author: Oliver Boorstein
Credits: N/A
calculate some statistics from population.json
'''

import json


def read_data(file_name: str, keys: list) -> list:

    fin = open(file_name)

    data = json.load(fin)



    
    for index in range(len(data)):
        newlist = [x for x in data[index]]
    #     for key in keys:

    #         pass
    #         # print(data[index][key])
    return newlist


print(read_data("CS210W24\projects\proj6\population.json", ["pop2023", "growth"]))