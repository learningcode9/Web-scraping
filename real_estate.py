import requests
from bs4 import BeautifulSoup
import csv
import pandas

url="https://www.century21.com/real-estate/walnut-creek-ca/LCCAWALNUTCREEK/"
data=requests.get(url)
soup=BeautifulSoup(data.content,'html.parser')
#print(soup)
all=soup.find(class_="infinite-container")
#print(all)
properties=all.find_all(class_="property-card-primary-info")
#print(properties)
price_home=[contents.find('a',class_='listing-price').text.replace("\n","") for contents in properties]
bedrooms_home=[contents.find('div',class_='col-wrap-mid').text.replace("\n","") for contents in properties]
sqft_home=[contents.find('div',class_="property-sqft").text.replace("\n","") for contents in properties]
address=[contents.find('div',class_="property-address").text.replace("\n","") for contents in properties]
city_home=[contents.find('div',class_="property-city").text.replace("\n","") for contents in properties]  
    
    #bedrooms=details.find('div',class_='property-beds')
    #bathrooms=details.find('div',clas_='property-baths')

df=pandas.DataFrame(
    {
        'price':price_home,
        'bedrooms&bathrooms':bedrooms_home,
        'sqft':sqft_home,
        'location':address,
        'city':city_home,
    }
)
df.to_csv('homes1.csv')