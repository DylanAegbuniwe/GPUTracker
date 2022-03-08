#!/opt/homebrew/bin/python3

# Author(s): Shaun Derstine
# Last Edit: 
# Description: 

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from sys import argv
from datetime import datetime

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

def main():
	# url is saved as a string
	url = argv[1]

	soup = convert_url(url)

	# li element that holds current price info
	li_elem = soup.find("li", class_="price-current")

	cur_price = ""

	# starting from index 1 in the children of the li element,
	# $, dollar amount, cent amount
	for i in range(1, len(li_elem.contents)):
		cur_price += li_elem.contents[i].string

	print("Price as of %s: %s" % (datetime.now(), cur_price))
	# store in dictionary { "Date":datetime.now(), "Price":cur_price }
# end main() 

if __name__ == "__main__":
	main()
