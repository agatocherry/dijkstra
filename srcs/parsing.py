# Description: Parse the data from the input file

from color import *
from utils import *

# * Search and save the input file
def save_file(file_name):
    try:
        f = open(file_name, "r")
        file = f.read()
        return file
    except:
        print(f"Error: {file_name} is not a file or can't be opened.")

def already_in_array(node, n):
    i = 0
    size = len(node)
    while(i < size):
        if (n == node[i]):
            return -1
        i += 1
    return 1

def search(node, nb):
    i = 0
    size = len(node)
    while (nb != node[i] and size > 0):
        i += 1
        size -= 1
    return i

# * Parse the node from the input file
def parse_node(file):
    i = 0
    node = []
    while (i < len(file)):
        if (i == 0 or file[i - 1] == '\n') and file[i] == 'e': 
            while(file[i] != ' '):
                i += 1
            while(file[i] == ' '):
                i += 1
            to_save = nb_entier(file, i)
            if (already_in_array(node, to_save) == 1):
                node.append(to_save)
            while(file[i] != ' '):
                i += 1
            while(file[i] == ' '):
                i += 1
            to_save = nb_entier(file, i)
            if (already_in_array(node, to_save) == 1):
                node.append(to_save)
        else:
            i += 1
    return node

def search_edge(file, i):
    edge = ""
    i += 1
    while(i < len(file) and file[i] == ' '):
        i += 1
    if (i < len(file) and file[i] == '\n'):
        return ("")
    while(i < len(file) and file[i].isdigit()):
        edge += file[i]
        i += 1
    return (edge)

# * Parse the data from the input file
def parse_data(file, node):
    data = [[-1 for i in range(len(node))] for j in range(len(node))]
    i = 0
    while (i < len(file)):
        if (i == 0 or file[i - 1] == '\n') and file[i] == 'e': 
            while(file[i] != ' '):
                i += 1
            while(file[i] == ' '):
                i += 1
            nb1 = nb_entier(file, i)
            while(file[i] != ' '):
                i += 1
            while(file[i] == ' '):
                i += 1
            nb2 = nb_entier(file, i)
            edge = search_edge(file, i)
            if (edge == ""):
                print(HRED + "Error: " + "The edge " + nb1 + " " + nb2 + " don't have any edge.")
                exit(1)
            data[search(node, nb1)][search(node, nb2)] = atoi(edge)
        else:
            i += 1
    j = 0
    return data