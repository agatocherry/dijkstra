# * Search and save the input file
def save_file(file_name):
    try:
        f = open(file_name, "r")
        file = f.read()
        print(file)
        return file
    except:
        print(f"Error: {file_name} is not a file or can't be opened.")

def parsing(file):
    i = 0
    # Faire un double tableau avec 0 si rien, et les distance des arrêtes si qlq choses
    # Faire un double tableau de 2* la taille de nodes
    # Faire un tableau simple de 0 à taille nodes : 'A' 'B' 'C' par exemple (pour connaitre ou cherche dans mon double tableau par rapport aux nodes)
    node = []
    print(len(file))
    size = len(file)
    while (i < size):
        if (i == 0 or file[i - 1] == '\n') and file[i] == 'e': 
            # Each start of the line
            # if (file[i] == 'e'):
            while(file[i] != ' '):
                i += 1
            while(file[i] == ' '):
                i += 1
            node.append(file[i])
            print(f"First node of the line {i}: {file[i]}")
            while(file[i] != ' '):
                i += 1
            while(file[i] == ' '):
                i += 1
            node.append(file[i])
            print(f"Second node of the line {i}: {file[i]}")
            # TODO: Rechercher si la node est pas déjà dans le tableau sinon pas save
        else:
            i += 1
    print(node[0])
    print(len(node))


file_name = input("What is the name of the file with the graph ? ")
file = save_file(file_name)
if file != None:
    parsing(file)