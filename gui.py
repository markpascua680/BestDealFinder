import PySimpleGUI as gui

# GUI color theme
gui.theme('DarkGrey6')

# Window specifications
width = 1024
height = 768

font = ('Candara', 12)  # Font name, font size
titleFont = ('Candara', 24)

# Elements on window
brands = ['AMD', 'Astro', 'ASUS', 'CoolerMaster', 'Corsair', 'EVGA', 'G.Skill', 'Gigabyte', 'Hyper X', 'Intel', 'Logitech', 'MSI', 'Nvidia', 'NZXT', 'Razer', 'Steelseries', '-None-']
accessories = ['CPU', 'Graphics Card', 'HDD', 'Keyboard', 'Motherboard', 'Mouse', 'PC Case', 'PC Fans', 'PC Headset', 'Power Supply', 'RAM', 'SSD']

brandList = [
            gui.Text("Select a brand", font=font),
            gui.Combo(values=brands, size=(20, 12), enable_events=True, key='-BRAND-')
            ]

accessoryList = [
                gui.Text("Select an accessory", font=font),
                gui.Combo(values=accessories, size=(20, 12), enable_events=True, key='-ITEM-')
                ]

layout = [
         [gui.Text("Best Deal Finder", size=(width, 1), font=titleFont, justification='center')],
         [gui.Text("Select sites to search from:", font=font),
                gui.Checkbox('Amazon', font=font, default=False, key='-AMAZON-'), 
                gui.Checkbox('BestBuy', font=font, default=False, key='-BESTBUY-'), 
                gui.Checkbox('B&H', font=font, default=False, key='-B&H-'), 
                gui.Checkbox('Newegg', font=font, default=False, key='-NEWEGG-'), 
                gui.Checkbox('Walmart', font=font, default=False, key='-WALMART-')
                ],
         brandList,
         accessoryList,
         [gui.Button("Submit", font=font), gui.Button("Exit", font=font)],
         [gui.Text("", font=font, key='-RESULTS-')]
         ]

# Create window
window = gui.Window("Best Deal Finder", layout, size=(width, height))

# Event loop
while True:
    # The "values" variable stores the values of user's inputs, whose keys are always indicated by hyphens on both sides of the key name e.g. -ITEM-
    event, values = window.read()
    
    # Updates the -RESULTS- variable to display items
    if event == "Submit":
        # Scrape from websites
        window['-RESULTS-'].update('Searching...')
    
    # Close window if Exit button is clicked
    if event == "Exit" or event == gui.WIN_CLOSED:
        break

    # Scrape from websites    
    if values['-AMAZON-'] is True:
        # Gather Amazon items
        pass
    
    if values['-BESTBUY-'] is True:
        # Gather BestBuy items
        pass
    
    if values['-B&H-'] is True:
        # Gather B&H items
        pass
    
    if values['-NEWEGG-'] is True:
        # Gather  items
        pass

    if values['-WALMART-'] is True:
        # Gather Walmart items
        pass


window.close()