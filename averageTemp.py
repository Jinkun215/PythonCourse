
def get_average():
    with open("files/temperature.txt", "r") as file:
        list_temp = file.readlines()

    total = [float(t) for t in list_temp]

    try:
        avg = sum(total) / len(total)
    except ZeroDivisionError:
        print("can't divide by zero")

    return avg


average_temp = get_average()
print(average_temp)
