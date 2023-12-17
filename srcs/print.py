# Description: Print functions for the project

from color import *

def longest_number(data):
    i = 0
    nbmaxsize = -1
    while(i < len(data)):
        j = 0
        while(j < len(data[i])):
            if (len(str(data[i][j])) > nbmaxsize):
                nbmaxsize = len(str(data[i][j]))
            j += 1
        i += 1
    return (nbmaxsize)

# * Print the data array
def print_data(node, data):
    print(RED + "Data array:" + RESET)
    lnumber = longest_number(data)
    if (longest_number(node) > lnumber):
        lnumber = longest_number(node)
    i = 0
    while(i < lnumber):
        print(" ", end="")
        i += 1
    i = 0
    while (i < len(node)):
        print(f"{node[i]:>{lnumber}}", end=" ")
        i += 1
    print()
    i = 0
    while(i < len(data)):
        j = 0
        print(f"{node[i]}", end=" ")
        while(j < len(data[i])):
            print(f"{data[i][j]:>{lnumber}}", end=" ")
            j += 1
        print()
        i += 1