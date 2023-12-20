# Description: Main file of the project

from color import *
from print import *
from parsing import *
from utils import *
import sys

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
    print_kruskal(node, data)