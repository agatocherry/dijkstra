# Description: Main file of the project

from color import *
from print import *
from parsing import *
from utils import *
import sys

# TODO print the order of each edge (min to max) (edge order : [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])
# TODO add a more complex graph (with more nodes and edges)

# * Search and give the input file
if len(sys.argv) != 2:
    print(HRED + "Error: You need to give a file as argument." + RESET)
    exit(1)
print(RED + "File: " + RESET + sys.argv[1])
file = save_file(sys.argv[1])
if file != None:
    node = parse_node(file)
    data = parse_data(file, node)
    print_data(node, data)
    print_neigbors(node, data)
    print_edge_order(node, data)