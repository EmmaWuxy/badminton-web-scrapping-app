from bs4 import BeautifulSoup as bs
from datetime import date
import os
import pandas as pd
import PySimpleGUI as sg
import requests
from src.create_output_table import create_output_table
from src.geo_util import geo_util

def get_badminton_centers():
    # Ask for customer location
    #postal_code = input("Please Enter Your Postal Code: ")
    
    # Get a list of recreation centers
    data_source = "https://www.toronto.ca/data/parks/prd/facilities/recreationcentres/index.html" # Put in config file 
    
    headers = {
        'X-Requested-With': 'XMLHttpRequest'
    }
    url = 'https://www.toronto.ca/data/parks/live/locations/centres.json?_=1655614708813'
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Web Page Not Accessible.")
        quit()
    
    data = response.json()
    df = None
    
    # Query each center page
    for center in data['all']:
        ctr_response = requests.get('https://www.toronto.ca/data/parks/prd/facilities/complex/' + str(center['ID']) + '/index.html')
        ctr_soup = bs(ctr_response.content, 'html.parser')
        try:
            data_curweek = ctr_soup.find('div',{'id': 'content_dropintype_Sports'}).find('table').find('tr', {'id':'dropin_Sports_0'})
            rows = data_curweek.find('tbody').find_all('tr')
        except AttributeError:
            #print('skip')
            continue
    
        # Scrap dates of current week (Check if today is in week_days)
        week_days = [ day.text.strip() for day in data_curweek.find_all('th', scope = 'col') ][1:]
        for day in week_days:
            if date.today().strftime("%b %d") in day:
                if df is None:
                    df = pd.DataFrame(columns = ['Address', 'District', 'km'] + week_days)
                break 
        else:
            continue
    
        # Scrap data for each row in the table
        for row in rows:
            header = row.find('th')
            if header is not None:
                if header.find('span', string = 'Badminton', attrs = {'class': 'coursetitlecol'}) is not None\
                and header.find('span', string = ' (18yrs and over)' or ' (19yrs and over)', attrs = {'class': 'courseagecol'}) is not None :
                    
                    # Scrap location and time
                    location_name = ctr_soup.find('h1').text.strip() # Location
                    df.loc[location_name, ['Address']] = ctr_soup.find('span', attrs = {'class': 'badge'}).find(text = True).strip()
                    df.loc[location_name, ['District']] = ctr_soup.find('span', attrs = {'class': 'addressbar'}).find('strong').text
                    df.loc[location_name, ['km']] = geo_util.get_interdistance(user_postal, geo_util.get_loc_postal_code(df.at[location_name, 'Address']))
                    for count, time in enumerate(row.find_all('td', attrs = {'class': 'coursehrscol'})):
                        if len(time.text) > 1:
                            df.loc[location_name, [week_days[count]]] = time.text
                        else:
                            df.loc[location_name, [week_days[count]]] = 'NA'
                    break
    df = df.sort_values('km', ascending=True)

    try:
        df.to_excel('output.xls')
    except PermissionError:
        print('Permission error when trying to write to output.xls... It might be caused by output.xls open on your desktop.')
    else:
        print('Work done successfully. Please view {} for results.'.format(os.getcwd() + '\output.xsl'))

    return ['Recreation Center'] + df.columns.values.tolist(), [[df.index.tolist()[i]] + r for i, r in enumerate(df.values.tolist())]


sg.theme('DarkBlue3')
sg.set_options(font=('Courier New',17))
layout = [[sg.Text('This app will display all recreation centers in Toronto that offers\nbadminton drop-in sessions that only open to adults in age group 18-60\nin the current week',text_color='Black')],
[sg.Text('Enter your postal code:')], [sg.Input(key = 'POSTAL_CODE', size = 14)], 
[sg.Text('Number of closest centers to display:')], [sg.Input(key = 'NUM_RECORDS', size = 14)], 
[sg.Text(key = 'INPUT_CHECK',text_color='Red')], [sg.Button('SHOW TABLE')]]
window = sg.Window('Badminton Web Scrapping App', layout, size = (1000,500))

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED or event is None:
        break
    user_postal = values['POSTAL_CODE']
    num_display = values['NUM_RECORDS']
    if event == 'SHOW TABLE':
        if geo_util.check_postal_code_format(user_postal) is False:
            window['INPUT_CHECK'].update('Invalid Postal Code! ex. H3G 5B4')
        elif num_display == '':
            headings, table = get_badminton_centers()
            create_output_table.create(headings, table, None)
        elif num_display.isdigit() is False:
            window['INPUT_CHECK'].update('Number much be positive integer!')
        else:
            headings, table = get_badminton_centers()
            create_output_table.create(headings, table, int(num_display))

window.close()