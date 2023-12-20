# Description: Kruskal algorithm for the project

from color import *
from utils import *

def search_node(node, nb):
    i = 0
    while (i < len(node)):
        inode = atoi(node[i])
        
        if (nb == inode):
            return i
        i += 1
    return 0

def is_sorted(node, data, edge):
    i = 0
    while(i < len(edge) - 1):
        j = 0
        if (data[search_node(node, atoi(edge[i][0]))][search_node(node, atoi(edge[i][1]))] > data[search_node(node, atoi(edge[i+1][0]))][search_node(node, atoi(edge[i+1][1]))]):
            return 0
        i += 1
    return 1

# * Kruskal algorithm: sort the edges by weight
def sort(node, data):
    i = 0
    edge = []
    while(i < len(node)):
        j = 0
        while(j < len(data[i])):
            if (data[i][j] > 0):
                edge.append((node[i], node[j]))
            j += 1
        i += 1
    while (is_sorted(node, data, edge) == 0):
        i = 0
        while(i < len(edge) - 1):
            j = 0
            if (data[search_node(node, atoi(edge[i][0]))][search_node(node, atoi(edge[i][1]))] > data[search_node(node, atoi(edge[i+1][0]))][search_node(node, atoi(edge[i+1][1]))]):
                tmp = edge[i]
                edge[i] = edge[i + 1]
                edge[i + 1] = tmp
            i += 1
    return edge

def kruskal(node, data, edge):
    vec = node.copy()
    save = []
    i = 0
    while (i <= len(node)):
        if (vec[search_node(node, edge[i][0])] != -1 and search_node(node, atoi(edge[i][1])) != -1 and search_node(node, atoi(edge[i][0])) != -1):
            vec[search_node(node, atoi(edge[i][0]))] = -1
            if (search_node(node, atoi(edge[i][1])) != -1):
                vec[search_node(node, atoi(edge[i][1]))] = -1
            save.append((edge[i][0], edge[i][1]))
        else:
            if (vec[search_node(node, atoi(edge[i][1]))] != -1):
                vec[search_node(node, atoi(edge[i][0]))] = -1
                vec[search_node(node, atoi(edge[i][1]))] = -1
                save.append((edge[i][0], edge[i][1]))
        i += 1
    for i in range(vec.count(-1)):
        vec.remove(-1)
    if (len(vec) > 1):
        print(f"{HRED}Error: The graph is not connected{RESET}")
        exit(1)
    return save