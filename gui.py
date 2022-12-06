import PySimpleGUI as gui
from Websites import *

# GUI color theme
gui.theme('DarkGrey6')

# Window specifications
width = 1920
height = 1080

font = ('Candara', 12)  # Font name, font size
titleFont = ('Candara', 24)

# Elements on window
brands = ['AMD', 'Astro', 'ASUS', 'CoolerMaster', 'Corsair', 'EVGA', 'G.Skill', 'Gigabyte', 'Hyper X', 'Intel', 'Logitech', 'MSI', 'Nvidia', 'NZXT', 'Razer', 'Steelseries', '-None-']
# accessories = ['CPU', 'Graphics Card', 'HDD', 'Keyboard', 'Motherboard', 'Mouse', 'PC Case', 'PC Fans', 'PC Headset', 'Power Supply', 'RAM', 'SSD']

brandList = [
            gui.Text("Select a brand", font=font),
            gui.Combo(values=brands, size=(20, 12), enable_events=True, key='-BRAND-')
            ]

# accessoryList = [
#                 gui.Text("Select an accessory", font=font),
#                 gui.Combo(values=accessories, size=(20, 12), enable_events=True, key='-ITEM-')
#                 ]

layout = [
         [gui.Text("Best Deal Finder", size=(width, 1), font=titleFont, justification='center')],
         [gui.Text("Select sites to search from:", font=font),
                gui.Checkbox('Amazon', font=font, default=False, key='-AMAZON-'),
                gui.Checkbox('Acer', font=font, default=False, key='-ACER-'), 
                gui.Checkbox('BestBuy', font=font, default=False, key='-BESTBUY-'), 
                gui.Checkbox('B&H', font=font, default=False, key='-B&H-'), 
                gui.Checkbox('Dell', font=font, default=False, key='-DELL-'),
                gui.Checkbox('Newegg', font=font, default=False, key='-NEWEGG-'), 
                gui.Checkbox('Walmart', font=font, default=False, key='-WALMART-')
                ],
         [gui.Text("Input search term: ", font=font), gui.InputText(key='-SEARCHTERM-')],
         brandList,
         # accessoryList,
         [gui.Button("Submit", font=font), gui.Button("Exit", font=font)],
         [gui.Text("", font=font, key='-RESULTS-')]
         ]

# Create window
window = gui.Window("Best Deal Finder", layout, size=(width, height))

def websiteChecked():
    if (    
            values['-AMAZON-'] == False and
            values['-ACER-'] == False and
            values['-BESTBUY-'] == False and
            values['-B&H-'] == False and
            values['-DELL-'] == False and
            values['-NEWEGG-'] == False and
            values['-WALMART-'] == False    
       ):
        return False
    return True

def itemEntered():
    if values['-SEARCHTERM-'] == "":
        return False
    return True

# Event loop
while True:
    # The "values" variable stores the values of user's inputs, whose keys are always indicated by hyphens on both sides of the key name e.g. -ITEM-
    event, values = window.read()
    
    # Updates the -RESULTS- variable to display items
    if event == "Submit":
        # Error checks
        # Check if at least one website box was checked
        if not websiteChecked():
           window['-RESULTS-'].update("Please select at least one website to search")
        # Check if an item was entered in search field
        elif not itemEntered():
           window['-RESULTS-'].update("Please enter an item")

        # Scrape from websites
        else:
            window['-RESULTS-'].update('Searching...')
            results = ""
            output = [[]]
            if values['-AMAZON-'] is True:
                # Gather Amazon items
                filter = [1, 1, 1]
                output.append(AmazonRequest(str(values['-BRAND-']), str(values['-SEARCHTERM-']), 4, filter))
                pass
            
            if values['-ACER-'] is True:
                # Gather Amazon items
                filter = [1, 1, 1]
                output.append(AcerRequest(str(values['-BRAND-']), str(values['-SEARCHTERM-']), 4, filter))
                pass
            
            if values['-BESTBUY-'] is True:
                # Gather BestBuy items
                filter = [1, 1, 1]
                output.append(BestBuyRequest(str(values['-BRAND-']), str(values['-SEARCHTERM-']), 4, filter))
                pass
            
            if values['-B&H-'] is True:
                # Gather B&H items
                filter = [1, 1, 1]
                output.append(BHRequest(str(values['-BRAND-']), str(values['-SEARCHTERM-']), 4, filter))
                pass
            
            if values['-DELL-'] is True:
                # Gather Amazon items
                filter = [1, 1, 1]
                output.append(DellRequest(str(values['-BRAND-']), str(values['-SEARCHTERM-']), 4, filter))
                pass
            
            if values['-NEWEGG-'] is True:
                # Gather  items
                filter = [1, 1, 1]
                output.append(NeweggRequest(str(values['-BRAND-']), str(values['-SEARCHTERM-']), 4, filter))
                pass

            if values['-WALMART-'] is True:
                # Gather Walmart items
                filter = [1, 1, 1]
                output.append(WalmartRequest(str(values['-BRAND-']), str(values['-SEARCHTERM-']), 4, filter))
                pass
            
            for item in output:
                for product in item:
                    results += product + '\n'

            window['-RESULTS-'].update(results)
            
    # Close window if Exit button is clicked
    if event == "Exit" or event == gui.WIN_CLOSED:
        break

    


window.close()