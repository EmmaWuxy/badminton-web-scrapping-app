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
print(response)
if response.status_code != 200:
    print("Web Page Not Accessible.")
    quit()

data = response.json()
# Query each center page
for center in data['all']:
    ctr_response = requests.get('https://www.toronto.ca/data/parks/prd/facilities/complex/' + str(center['ID']) + '/index.html')
    ctr_soup = bs(ctr_response.content, 'html.parser')
    try:
        rows = ctr_soup.find('div',{'id': 'content_dropintype_Sports'}).find('table').find('tr', {'id':'dropin_Sports_0'}).find('tbody').find_all('tr')
    except AttributeError:
        #print('skip')
        continue
    #else:
        #print('Did not skip')
    for row in rows:
        header = row.find('th')
        if header is not None:
            #print('here')
            if header.find('span', string='Basketball', attrs={'class': 'coursetitlecol'}) is not None\
            and header.find('span', string=' (6 - 9yrs)', attrs= {'class': 'courseagecol'}) is not None :
                print(ctr_soup.find('h1').text)
                print(ctr_soup.find('span', attrs={'class': 'badge'}).text)
                print(ctr_soup.find('span', attrs={'class': 'addressbar'}).find('strong').text)
                for time in row.find_all('td', string = lambda s: len(s)>1, attrs={'class': 'coursehrscol'}):
                    print(time.text)
                break


#soup = bs(data['all'])
#print(soup)
#links = soup.findAll('a')
#for link in links:
#    print(link.text)

# Web scraping Logic
 # Get a list of ID's
 # Create for loop to get the ID

# Convert to Excel