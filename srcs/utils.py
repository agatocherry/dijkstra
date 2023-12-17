# Description: Utils functions for the project

from color import *

def atoi(c):
    return max(min(int(c), 2**31 - 1), -2**31) if c.strip() else 0

def nb_entier(file, i):
    to_transform = ""
    while(file[i].isdigit()):
        to_transform += file[i]
        i += 1
    return (to_transform)