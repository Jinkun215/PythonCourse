
# This would not run if file doesn't exist (FileNotFoundError)

# with open("files/exists.txt", "r") as file:
#     new_file = file.read()

# print(new_file)


#This would run.  If File doesn't exist, it will create it first.

try:
    with open("files/exists.txt", "r") as file:
        new_file = file.read()
except FileNotFoundError:
    with open("files/exists.txt", "w") as file:
        file.write("File Exists!")
    with open("files/exists.txt", "r") as file:
        new_file = file.read()

print(new_file)

