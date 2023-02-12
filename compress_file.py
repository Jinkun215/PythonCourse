import PySimpleGUI as psg

label1 = psg.Text("Select file to compress")
input1 = psg.Input()
choose_button1 = psg.FilesBrowse("Choose")

label2 = psg.Text("Select destination folder")
input2 = psg.Input()
choose_button2 = psg.FolderBrowse("Choose")

compress_button = psg.Button("Compress")

window = psg.Window("File Compression App", layout=[[label1, input1, choose_button1],
                                                    [label2, input2, choose_button2],
                                                    [compress_button]])


window.read()
window.close()