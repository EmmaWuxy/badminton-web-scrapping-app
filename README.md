# badminton-web-scrapping-app
A simple Web Scraping App that scraps all the recreation centers in Toronto that offers badminton drop-in sessions for adults in age group 18-60 in the current week. The app stores the recreation center's name, address, district, available session dates and time in Excel file output.xls in current working directory.

Data source: latest data posted by Toronto Park on their website : https://www.toronto.ca/data/parks/prd/facilities/recreationcentres/index.html 

## Dependencies
Compatible OS: Windows 10\
Python 3.7.2\
beautifulsoup4==4.11.1\
pandas==0.25.1\
requests==2.23.0\
PySimpleGUI==4.60.1

## How to Run Code
Install dependencies
```
~$ pip install -r badminton-web-scrapping-app/requirements.txt
```
Run application from CLI
```
~$ python badminton-web-scrapping-app
```
## Result Example Screenshot
The result of running the application will be print out on GUI, and store in output.xsl in your current working directory.
GUI
<br>
<img src="https://github.com/EmmaWuxy/badminton-web-scrapping-app/blob/main/images/gui_1.png"/>
<br>
<br>
<img src="https://github.com/EmmaWuxy/badminton-web-scrapping-app/blob/main/images/gui_2.png"/>
<br>
output.xsl
<br>
<img src="https://github.com/EmmaWuxy/badminton-web-scrapping-app/blob/main/images/result_example.png"/>
<br>
