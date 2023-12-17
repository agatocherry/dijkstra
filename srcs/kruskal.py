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
    return -1

def is_sorted(node, data, edge):
    i = 0
    while(i < len(edge) - 1):
        j = 0
        if (data[search_node(node, atoi(edge[i][0]))][search_node(node, atoi(edge[i][1]))] > data[search_node(node, atoi(edge[i+1][0]))][search_node(node, atoi(edge[i+1][1]))]):
            return 0
        i += 1
    return 1

# * Kruskal algorithm: sort the edges by weight
def kruskal(node, data):
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