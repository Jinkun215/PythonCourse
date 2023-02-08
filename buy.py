
while True:
    with open("files/probability.txt", "r") as file:
        sides = file.readlines()

    flip = input("Enter head or tail: ") + "\n"
    flip = flip.capitalize()

    sides.append(flip)
    numOfHead = sides.count("Head\n")       #Make sure \n is there, or will always be 0%
    percentage = float(numOfHead) / len(sides) * 100.0
    #print("Heads: " + str(percentage) + "%")
    print(f"Heads: {percentage}%")          #using f-string keeps things neater

    with open("files/probability.txt", "w") as file:
        file.writelines(sides)

