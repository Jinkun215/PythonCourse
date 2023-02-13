import functions
import PySimpleGUI as psg

label = psg.Text("Enter in a to-do")
input_box = psg.InputText(tooltip="Enter todo", key="todo")
add_button = psg.Button("Add")
list_box = psg.Listbox(values=functions.f_readFile(), key="todos",
                       enable_events=True, size=(45,10))
edit_button = psg.Button("Edit")



window = psg.Window("My To-Do App",
                    layout=[[label], [input_box, add_button], [list_box, edit_button]],
                    font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values["todos"])
    match event:
        case "Add":
            todos = functions.f_readFile()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.f_writeFile(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"] + "\n"
            todos = functions.f_readFile()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.f_writeFile(todos)
            window['todos'].update(values=todos)

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case psg.WIN_CLOSED:
            break

window.close()