import requests
from bs4 import BeautifulSoup
import pandas
import csv

url="https://www.indeed.com/jobs?q=Junior+Web+Developer+Python&l=San+Francisco+Bay+Area%2C+CA&radius=50"

data=requests.get(url)
soup=BeautifulSoup(data.content,'html.parser')
content=soup.find(id="resultsCol")
#print(content.prettify())
#f = csv.writer(open('indeed.csv', 'w'))
#f.writerow(['role','name','loation'])
final=content.find_all('div',class_='jobsearch-SerpJobCard')



#for contents in content:
result_ti=[contents.find('div',class_='title').text.replace("\n","") for contents in final]
#print(result_ti)
company_co=[contents.find('span',class_='company').text.replace("\n","") for contents in final]
#print(company_co)
place_lo=[contents.find('div',class_='sjcl').find(class_='location').text.replace("\n","") for contents in final]
#print(place_lo)
#company_lo=[contents.find('div',class_='sjcl').find('span.text.replace("\n","") for contents in final]
#print(company_lo)
#place_lo=[contents.find('span',class_='sjcl').text.replace("\n","") for contents in final]
#print(place_lo)
#print(place)
#if (result_ti,company_co,place_lo) is None:
   #continue
#role=[result_ti.get_text().replace("\n","").replace(",","")]
#print(role)
#name=company_co.text.replace("\n","").replace(",","")
#print(name)
#location=place_lo.text.replace("\n","").replace(",","")
#print(location)
    #f.writerow([role,name,location])
pd=pandas.DataFrame(
    {
       'role':result_ti,
       'company':company_co,
       'location':place_lo,
    }

)
pd.to_csv('indeed1.csv')


    