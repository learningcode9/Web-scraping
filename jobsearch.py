import requests
from bs4 import BeautifulSoup
import pandas
import csv

URL = 'https://www.monster.com/jobs/search/?q=entry-level-python-developer&where=Sfo'
page=requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')
inside=soup.find(id='SearchResults')
#print(inside)
job_elem=inside.find_all(class_='summary')
print(job_elem)
#for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
#title_elem = [job_elem.find('h2', class_='title').get_text() for job_elem in job_elems]
#print(title_elem)
    #company_elem = job_elem.find('div', class_='company')
    #location_elem = job_elem.find('div', class_='location')
    #print(title_elem)
    #print(company_elem)
    #print(location_elem)
    

#print(deep)
#jobrole=[box.find(class_='card-header').text for box in deep]
#print(jobrole)
#job_stuff=pandas.DataFrame(
 #       {
  #          'location':location_elem,
   #         'job role':title_elem,
    #        'company':company_elem,        
     #   }
    #)
#print(job_stuff)
    
   

    
  


   



