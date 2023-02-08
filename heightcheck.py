def convert_ItoM(height_inches):
    print(f"You are {height_inches * 0.0254} meter tall.")
    return height_inches * 0.0254;

def RidePass(height_meter):
    if (height_meter >= 1.0):
        print("You can ride")
    else:
        print("Too short")

def Parse(height):
    parts = height.split(" ")
    feet = float(parts[0])
    inch = float(parts[1])
    return {"feet" : feet, "inch" : inch}

#myHeight = float(input("Enter height in inches: " ))

#RidePass(convert_ItoM(myHeight))

myHeight = input("Enter Feet and Inch: ")
myList = Parse(myHeight)
print(myList)