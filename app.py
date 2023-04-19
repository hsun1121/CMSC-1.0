from pathlib import Path

import PySimpleGUI as sg
import pandas as pd
import numpy as np

from table import create_table
from enter_event import enter_data

# Add some color to the window
sg.theme('DarkTeal9')

# Home GUI window
layout = [
    [sg.Text('What would you like to do:')],

    [sg.Button('Add Event'), sg.Button('Show Events'), sg.Exit()]
]

window = sg.Window('Event Reminder App', layout)


# Control for home GUI window
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Add Event':
        enter_data()
    if event == 'Show Events':
        sg.popup('Event Page')

window.close()


