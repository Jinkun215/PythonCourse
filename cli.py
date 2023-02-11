#from functions import f_readFile, f_writeFile
import functions
import time

# print(help(f_readFile))
#print(help(f_writeFile))

#added comment

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is currently", now)
while True:
    myInput = input("Enter add, show, edit, complete, or exit:  ")
    myInput = myInput.strip().lower()


    todo_list = functions.f_readFile()

    if myInput.startswith("add"):
        myInput = myInput[4:] + "\n"

        todo_list.append(myInput.capitalize())

        functions.f_writeFile(listArg=todo_list)  #purposely doing = version

    elif myInput.startswith("show"):

        stripped_todo_list = [i.strip('\n') for i in todo_list]

        for index, items in enumerate(stripped_todo_list):
            print(f"{index + 1}. {items}")

    elif myInput.startswith("edit"):
        try:
            editNum =  int(myInput[5:])
            myInput = input("Enter todo: ") + "\n"
            todo_list[int(editNum) - 1] = myInput

            functions.f_writeFile(todo_list)

        except (ValueError):
            print("Incorrect input.  Please use format: \"edit #\"")
        except (IndexError):
            print("Incorrect input.  Please select item within range.")


    elif myInput.startswith("complete"):
        try:
            editNum = int(myInput[9:])
            todo_list.pop(int(editNum) - 1)
            print(f"List item {editNum} has been completed.")

            functions.f_writeFile(todo_list)

        except (ValueError):
            print("Incorrect input.  Please use format: \"complete #\"")
        except (IndexError):
            print("Incorrect input.  Please select item within range.")


    elif myInput.startswith("exit"):
        break

    else:
        print("Unknown command, please try again.")

