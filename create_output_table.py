import PySimpleGUI as sg
import os

def create(headings, table_array):
    sg.set_options(font=('Courier New',7))
    table_layout = [[sg.Text('Adult Drop-in Badminton Sessions Available This Week (sort by distance):')], 
    [sg.Table(values = table_array, headings = headings, key = '-OUTPUT-', auto_size_columns = False, display_row_numbers = True, row_height = 30, col_widths=[40,40,20,10,16,16,16,16,16,16,16])],
    [sg.Text('The talbe is also stored in {}\output.xsl'.format(os.getcwd()))]]
    table_window = sg.Window("Badminton Center Information Window", table_layout, size = (1800,150))
    
    while True:
        event, values = table_window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED or event is None:
            break
    
    table_window.close()