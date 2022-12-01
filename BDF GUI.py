import PySimpleGUI as gui

# Elements on window
layout = [
         [gui.Text("Best Deal Finder")],
         [gui.Text("Input product name: "), gui.InputText(key='input')],
         [gui.Button("Submit"), gui.Button("Exit")],
         [gui.Text("Output: "), gui.Text(size=(15,1), key='output')],
         [gui.Text("Select sites to search from")],
         [gui.Checkbox('Amazon', default=False, key='Amazon'), gui.Checkbox('BestBuy', default=False, key='BestBuy'), gui.Checkbox('B&H', default=False, key='B&H'), gui.Checkbox('Newegg', default=False, key='Newegg'), gui.Checkbox('Walmart', default=False, key='Walmart')]
         ]

# Create window
width = 425
height = 175
window = gui.Window("Best Deal Finder", layout, size=(width, height))

# Event loop
while True:
    event, values = window.read()
    
    # Updates the -OUTPUT- variable to the string stored in -IN-
    if event == "Submit":
        window['output'].update(values['input'])
    
    # Close window if Exit button is clicked
    if event == "Exit" or event == gui.WIN_CLOSED:
        break
    
if values['Amazon'] is True:
    print("Amazon")

window.close()