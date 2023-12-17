# Description: Print functions for the project

from color import *
from utils import *
from kruskal import *

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

def is_minus(data):
    i = 0
    while(i < len(data)):
        j = 0
        while(j < len(data[i])):
            if (data[i][j] < 0):
                return (1)
            j += 1
        i += 1
    return (0)

# * Print the data array
def print_data(node, data):
    print(RED + "Data array:" + RESET)
    lnumber = longest_number(data)
    if (longest_number(node) > lnumber):
        lnumber = longest_number(node)
    i = 0
    lnode = longest_number(node)
    if (is_minus(data) == 1):
        lnode += 1
    while(i < lnode):
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

# * Make a list of the node neighbors
def print_neigbors(node, data):
    print(RED + "Neighbors list:" + RESET)
    i = 0
    while(i < len(node)):
        j = 0
        neighbors = []
        while(j < len(data[i])):
            if (data[i][j] > 0):
                neighbors.append(node[j])
            j += 1
        if (len(neighbors) > 0):
            print(f"Neighbors of {node[i]}: ", end="")
            for n in neighbors:
                print(f"{n}", end="")
                if (n != neighbors[-1]):
                    print(", ", end="")
            print()
        i += 1

# * Print the order of each edge (min to max) as: [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)]
def print_edge_order(node, data):
    print(RED + "Smallest to largest edge (Kruskal):" + RESET)
    edge = kruskal(node, data)
    print(edge)
    