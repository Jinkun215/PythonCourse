import functions
import PySimpleGUI as psg

label = psg.Text("Enter in a to-do")
input_box = psg.InputText(tooltip="Enter todo", key="todo")
add_button = psg.Button("Add")

window = psg.Window("My To-Do App",
                    layout=[[label], [input_box, add_button]],
                    font=("Helvetica", 20))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.f_readFile()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.f_writeFile(todos)
        case psg.WIN_CLOSED:
            break

window.close()