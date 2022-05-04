# Author(s): 	Shaun Derstine
# Date Created: 2/14/2022 
# Description: 	This program contains function(s) for retreiving the item name, price,
#		as-of date, and inventory status of a product listed on newegg

import mysql.connector
import sys
from time import sleep
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from datetime import date

# Input:	url
# Output: 	bs4 object
def convert_url(url):
	# urlopen makes a request to webpage at url
	# result is an object which is saved as url_object
	url_object = urlopen(url)

	# the raw html from the webpage is saved in html_doc
	html_doc = url_object.read()

	# converts raw html to BeautifulSoup object 'soup'
	soup = bs(html_doc, 'html.parser')

	return soup
# end convert_url()

# Input:	url to product page
# Output:	dictionary holding product details from given link
# Format:	{ 'product_title':'', 'current_price':'', 'last_updated':'', 'in_stock':bool }
def get_product(url):
	# convert url into bs4 object
	soup = convert_url(url)

	# PRODUCT TITLE
	product_title = soup.find('h1', class_='product-title').string

	# CURRENT PRICE
	li_elem = soup.find('li', class_='price-current')

	# starting from index 1 in the children of the li element,
	# $, dollar amount, cent amount
	cur_price = ''
	for i in range(1, len(li_elem.contents)):
		# concat each segment of current price to string
		cur_price += li_elem.contents[i].string

	# CURRENT DATE (yyyy-mm-dd)
	cur_date = date.today().isoformat()

	# INVENTORY STATUS
	product_inventory = soup.find('div', class_='product-inventory')
	inventory_status = product_inventory.find(string='In stock.') == 'In stock.'

	# return as dictionary
	return { 'product_title':product_title, 'current_price':cur_price, 'last_updated':cur_date, 'in_stock':inventory_status }
# end get_product()

# Input:	None
# Output:	Dictionary containing product details for top 36 best selling GPUs on Newegg
# Format:	{ 'item':[''], 'price':[''], 'date':[''], 'status':[''] }
def get_best_selling_gpus():
	# Convert webpage listing best selling GPUs into bs object
	link_to_best_selling_page = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709&Order=3'
	soup = convert_url(link_to_best_selling_page)

	# Get all GPUs listed on page into list
	gpus = soup.find_all('a', class_='item-title')

	# Dictionary to hold product details
	product_details = {
		'product_title':[],
		'current_price':[],
		'last_updated':[],
		'in_stock':[]
	}

	# Get product details for each GPU
	# Append values for each individual gpu to list of values in current dictionary

	# Maybe store gpu details in custom object gpu
	for gpu in gpus:
		details = get_product(gpu['href'])
		product_details['product_title'].append(details['product_title'])
		product_details['current_price'].append(details['current_price'])
		product_details['last_updated'].append(details['last_updated'])
		product_details['in_stock'].append(details['in_stock'])

	return product_details
# end get_best_selling_gpus()

# Attempt to establish a connection to mysql server
# Note: Avoid calling without including safe closure of connection
def connect_to_database():
	# Local variables
	num_fails = 0
	connected = False

	# Attempt to connect to mysql database
	# If unsuccessful on third attempt, script will exit
	while not connected:
		try:
			# Create connection to mySQL server
			connection = mysql.connector.connect(
				user='scraper', 
				password='scraper',
				host='db',
				database='gputracker'
			)
		except:
			num_fails += 1
			if num_fails >= 3:
				sys.exit("Unable to connect after three attempts")
			print("Connection failed. Trying again in 30 seconds...")
			sleep(30)
		else:
			connected = True
			print("Successfully connected to server.")

	# Return mysql connector object if successful
	return connection

	# Safely end connection to mysql server
	#connection.close()
# end connect_to_database()

# Populate database on mysql server with product info for top 36 best selling gpus on newegg.com
def write_to_database():
	# Establish connection to server
	connection = connect_to_database()

	# Create dictionary to more easily define tables
	tables = {}

	# Create string to define table
	tables['gpu_table'] = (
		"CREATE TABLE IF NOT EXISTS gpus ("
		"	gpu_id INT PRIMARY KEY AUTO_INCREMENT,"
		"	product_title VARCHAR(255),"
		"	current_price DECIMAL(8,2),"
		"	last_updated VARCHAR(255),"
		"	in_stock VARCHAR(255)"
		")"
	)

	# Create string to add gpu to table
	add_gpu = ( "INSERT INTO gpus "
		    "(product_title, current_price, last_updated, in_stock) "
		    "VALUES (%s, %s, %s, %s)" )
	

	# Initialize cursor to interact with database
	cursor = connection.cursor()

	# MODIFY DATABASE HERE
	# Create table 'gpus'
	cursor.execute(tables['gpu_table'])

	# Add gpu details to table 'gpus'
	gpus = get_best_selling_gpus()
	num_gpus = len(gpus['product_title'])

	# Loop through each gpu and add details to database
	for i in range(0, num_gpus):
		gpu_details = (
			str(gpus['product_title'][i]),
			# Set price to 0 if no price data is found
			0 if gpus['current_price'][i] == '' else gpus['current_price'][i][1:].replace(',',''),
			gpus['last_updated'][i],
			gpus['in_stock'][i]
		)
		# Combine generic insert values statement with specific gpu details and write to database
		cursor.execute(add_gpu, gpu_details)

	# Commit changes to server
	connection.commit()

	# Safely close cursor
	cursor.close()

	# Safely end connection to mysql server
	connection.close()
# end write_to_database()
