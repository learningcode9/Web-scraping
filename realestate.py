import requests
from bs4 import BeautifulSoup
import csv

url="https://www.century21.com/real-estate/walnut-creek-ca/LCCAWALNUTCREEK/"
data=requests.get(url)
soup=BeautifulSoup(data.content,'html.parser')
#print(soup)
all=soup.find(class_="infinite-container")
#print(all)
properties=all.find_all(class_="property-card-primary-info")
#print(properties)
f = csv.writer(open('homes.csv', 'w'))
f.writerow(['price', 'bedrooms','sqft','address','city'])


for details in properties:
    
    price_home=details.find('a',class_='listing-price')
    #bedrooms=details.find('div',class_='property-beds')
    #bathrooms=details.find('div',clas_='property-baths')
    bedrooms_home=details.find('div',class_='col-wrap-mid')
    sqft_home=details.find('div',class_="property-sqft")
    address_home=details.find('div',class_="property-address")
    city_home=details.find('div',class_="property-city")
    if (price_home,bedrooms_home,sqft_home,address_home,city_home) is None:
        continue
    price=price_home.text.replace(",","").replace(" ","")
    #print(price)
    bedrooms=bedrooms_home.text.replace(",","").replace(" ","")
    #print(bedrooms)
    sqft=sqft_home.text.replace(",","").replace(" ","")
    #print(sqft)
    address=address_home.text.replace(",","").replace(" ","")
    #print(address)
    city=city_home.text
    #print(city)
    f.writerow([price,bedrooms,sqft,address,city])

#print(df)

   