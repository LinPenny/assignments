#import all the tools
import requests, mechanize
from bs4 import BeautifulSoup
#create a variable and set it to the url of Boone County Jail website 
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
#create a mechanize browser, open the website and read its html
br = mechanize.Browser()
br.open(url)
html = br.response().read()
#make the html a beautiful soup project
soup = BeautifulSoup(html, "html.parser")
#find the main table with its <tbody> tag and its id "mrc_main_table"
main_table = soup.find('tbody',
    {'id': 'mrc_main_table'}
)
#create a row list that includes all rows in the main table
row_list = main_table.find_all('tr')

for r in row_list:
#find all cells in the rows
    cell_list = r.find_all('td')
#print the text in the cell if it's not empty and delete the whitespace at the beginning and the end of the text
    if len(cell_list) > 0:
        for c in cell_list:
            print c.text.strip()
#print "----------" to seperate different detainees' info
        print '----------'
#print "IT WORKED" at the end
print 'IT WORKED!'