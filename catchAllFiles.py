import glob

myFiles = glob.glob("starfolder/*.txt")

for filepath in myFiles:
    with open(filepath, "r") as fileread:
        print(fileread.read())