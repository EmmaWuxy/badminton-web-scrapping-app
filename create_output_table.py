import PySimpleGUI as sg
import os

def create(headings, table_array):
    sg.set_options(font=('Courier New',7))
    table_layout = [[sg.Text('Adult Drop-in Badminton Sessions Available This Week:')], 
    [sg.Table(values = table_array, headings = headings, key = '-OUTPUT-', max_col_width = 110, auto_size_columns = True, display_row_numbers = True, row_height = 20)],
    [sg.Text('The talbe is also stored in {}\output.xsl'.format(os.getcwd()))]]
    table_window = sg.Window("Badminton Center Information Window", table_layout)
    
    while True:
        event, values = table_window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
    
    table_window.close()