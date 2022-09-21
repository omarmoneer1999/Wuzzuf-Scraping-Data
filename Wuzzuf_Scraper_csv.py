#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing the required Libraries
import pandas as pd
from bs4 import BeautifulSoup as bs  
from urllib.request import urlopen
from requests_html import HTMLSession
session = HTMLSession()


# In[38]:


#getting the number of pages to add it as the range to extract the information from the pages
url= input("Enter the wanted job search page from Wuzzuf \n")
client = session.get(url)
# html = client.read()
# client.close()
soup=bs(client.content,'html.parser')
number = soup.find('li',{"class":"css-8neukt"}).text[-3:]
number


# In[39]:


company = []
job_title = []
work_place = []
work_type = []
link = []
experience = []
adding_time = []
for i in range(int(number)):
    url=url+str(i)
    client = session.get(url)
#     html = client.read()
#     client.close()
    soup=bs(client.content,'html.parser')
    containers = soup.find_all('div',{"class":"css-1gatmva e1v1l3u10"})
    for container in containers:
            jtitle = container.div.h2.text
            job_title.append(jtitle)
            
            h = container.find('a',{'class':'css-17s97q8'}).text
            h=h.split(" -")
            company.append(h[0])
            
            place = container.span.text
            work_place.append(place)
            
            w_type =container.find('span',{'class':'css-1ve4b75 eoyjyou0'}).text
            work_type.append(w_type)
            
            link_con = container.find('h2',{'class':'css-m604qf'})
            link_con =link_con.a.get('href')
            link.append("https://wuzzuf.net/"+link_con[1:])
            
            container2 = container.find('div',{'class',"css-y4udm8"})
            exper = container2.find('a',{'class':'css-o171kl'})
            exper =exper.text
            experience.append(exper)
            
            add = container.select_one(".css-4c4ojb, .css-do6t5g").text
            adding_time.append(add)
company


# In[40]:


adding_time


# In[41]:


# First way to save the data in CSV file 
df = pd.DataFrame()
df['job_title'] = job_title
df['adding_time'] = adding_time
df['company_name'] = company
df['work_type'] = work_type
df['work_place'] = work_place
df['link'] = link
df['experience'] = experience
df.to_csv('Search Result.csv', index=False)


# In[31]:


df.info()


# In[21]:


# Second way to save the data in CSV file
from itertools import zip_longest
import csv
file_list = [job_title,company,work_type,work_place,link,experience]
exported = zip_longest(*file_list)
with open(r"C:\Users\....\jobs.csv","w", encoding="utf-8") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(['job_title','company_name','work_type','work_place','link','experience'])
    wr.writerows(exported)

