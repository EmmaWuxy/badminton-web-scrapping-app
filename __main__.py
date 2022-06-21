import requests
from bs4 import BeautifulSoup as bs

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
    #else:
        #print('Did not skip')
    for row in rows:
        header = row.find('th')
        if header is not None:
            #print('here')
            if header.find('span', string = 'Badminton', attrs = {'class': 'coursetitlecol'}) is not None\
            and header.find('span', string = ' (18yrs and over)' or ' (19yrs and over)', attrs = {'class': 'courseagecol'}) is not None :
                # Scrap dates of current week
                week_days = [ day.text for day in data_curweek.find_all('th', scope = 'col') ][1:]

                # Scrap location and time
                print(ctr_soup.find('h1').text.strip()) # Location
                print(ctr_soup.find('span', attrs = {'class': 'badge'}).find(text = True).strip()) # Address
                print(ctr_soup.find('span', attrs = {'class': 'addressbar'}).find('strong').text) # District
                for count, time in enumerate(row.find_all('td', attrs = {'class': 'coursehrscol'})):
                    if len(time.text) > 1:
                        print(week_days[count]) # Date
                        print(time.text) # Time
                break

# Convert to Excel