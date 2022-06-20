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
r = requests.get('https://www.toronto.ca/data/parks/prd/facilities/complex/' + str(data['all'][1]['ID']) + '/index.html')
soup = bs(r.content, 'html.parser')
print(soup)
#for center in data['all']:
#    print('https://www.toronto.ca/data/parks/prd/facilities/complex/' + str(center['ID']) + '/index.html')


#soup = bs(data['all'])
#print(soup)
#links = soup.findAll('a')
#for link in links:
#    print(link.text)

# Web scraping Logic
 # Get a list of ID's
 # Create for loop to get the ID

# Convert to Excel