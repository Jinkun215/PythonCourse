K_FILEPATH = "files/todos.txt"



def f_readFile(filepath=K_FILEPATH):
    """ Return a List taken from a text file containing the to-do list. """
    with open(filepath, "r") as file:
        listArg = file.readlines()
    return listArg

def f_writeFile(listArg, filepath = K_FILEPATH):
    """ Write the to-do items List to a text file. """
    with open(filepath, "w") as file:
        file.writelines(listArg)

if __name__ == "__main__":
    print("Function File is being run outside of import")