#  William Sigala
#  CSE 3302
#  Lab 1
#  ID# 1001730022

#  compile: python3 wts0022_lab01.py

import os

def get_size(path):
    total = 0
    
    for elem in os.listdir(path):
        if os.path.isfile(f"{path}/{elem}"):
            total += os.path.getsize(f"{path}/{elem}")
        else:
            total += get_size(f"{path}/{elem}")
    return total

total_size = get_size(os.getcwd())
print(f"{total_size} bytes")