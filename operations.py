def get_price(cell):
    try:
     whole_number = str(cell.find_all("li", attrs={"class": "price-current"})).split("<strong>")[1].split("</strong")[0]
     decimal = str(cell.find_all("li", attrs={"class": "price-current"})).split("<sup>")[1].split("</sup")[0]
     price = whole_number + decimal
     price = float(price.replace(',', ''))
     return price
    except:
        pass



def get_name(cell):
    try:
        full_name = str(cell.find_all("a", attrs={"title": "View Details"})).split('>')[1].split('<')[0]
        return full_name
    except:
       pass

