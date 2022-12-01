import PySimpleGUI as gui

# Elements on window
layout = [
        [gui.Text("Testing testing")],
        [gui.Button("It worked!")]
    ]

# Create window
window = gui.Window("Best Deal Finder", layout, size=(350, 200))

# Event loop
while True:
    event, values = window.read()
    if event == "It worked!" or event == gui.WIN_CLOSED:
        break

window.close()