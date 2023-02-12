import PySimpleGUI as psg

label1 = psg.Text("Enter feet: ")
input_text1 = psg.Input()

label2 = psg.Text("Enter inches: ")
input_text2 = psg.Input()

convert_button = psg.Button("Convert")


window = psg.Window("Convertor", layout=[[label1, input_text1],
                                         [label2, input_text2],
                                         [convert_button]])
window.read()
window.close()