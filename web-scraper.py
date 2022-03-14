#!/opt/homebrew/bin/python3

# Author(s): Shaun Derstine and Justin Baksi
# Last Edit: 
# Description:

from urllib.request import urlopen as request
from bs4 import BeautifulSoup as soup
from datetime import date, datetime
import mysql.connector


#connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="JuanSoto^%OPS+",
  database= "gpu"
)
mycursor = mydb.cursor()

page = 1
while True:
	now = datetime.now()
	formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

	#there are only 100 pages for GPUs currently on newegg, so we will reset the count to 1 when we exceed the limit
	if page == 101:
		page = 1

	#the URL which we want to scrape. this is the page to preview all the graphics card. the page number will increment by one to account for all the pages.
	url = 'https://www.newegg.com/p/pl?d=graphics+cards&page=' + str(page)

	##grab the html from the page
	client = request(url)
	page_html = client.read()
	client.close()
	page_soup = soup(page_html, 'html.parser')
	cells = page_soup.find_all("div", attrs={"class": "item-cell"})


	#here we loop through each cell with "class = "item-cell"". on newegg, these are each gpu listed.
	for cell in cells:

		try:
			full_name = str(cell.find_all("a", attrs={"title": "View Details"})).split('>')[1].split('<')[0]
			#brand_name = full_name.split()[0]
			#print(page, i, brand_name, date.today().isoformat(), datetime.now().time())
		except:
			print("not a gpu")

		#insert the entry into our database
		try:
			sql = "INSERT INTO prices (gpuname, price, datetime) VALUES (%s, %s, %s)"
			val = (full_name, 600, formatted_date)
			mycursor.execute(sql, val)
			print("inserted entry into database")
		except: #if that gpu is already in our DB, we update the price and date :)
			sql = "UPDATE prices SET price = %s, datetime = %s WHERE gpuname = %s"
			val = (420.69, formatted_date, full_name)
			mycursor.execute(sql, val)
			print("updated")
	mydb.commit()

	#increment page by one
	page += 1

