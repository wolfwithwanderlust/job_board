#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

url = "https://www.meteojob.com/jobs?what=Data&where=Lyon"
response = requests.get(url)
if response.status_code == 200:
    htmlData = response.content
    soup = BeautifulSoup(htmlData, 'html.parser')

    job_listings = soup.find_all('div', class_='truncated-text-fix')
    jobs_data = []
    for job in job_listings:
        #metadataitems = job_listings('span', class="mr-1 mb-0 ng-star-inserted")
        title = job.find('h2').text.strip() if job.find('h2') else ''
        company = job.find(class_="d-inline-block mt-1 mb-0 ng-star-inserted").text.strip() if job.find(class_="d-inline-block mt-1 mb-0 ng-star-inserted") else ''
        types = job.find(class_="mr-1 mb-0 ng-star-inserted").text.strip() if job.find(class_="mr-1 mb-0 ng-star-inserted") else ''
        date = job.find(class_="cc-font-size-small").text.strip() if job.find(class_="cc-font-size-small") else ''
        salary = job.find(class_="cc-tag-primary-light").text.strip() if job.find(class_="cc-tag-primary-light") else ''

        jobs_data.append({"Titre": title,"Company": company,"Type_de_contrat": types,"date_de_publication":date,"salaire" :salary})
        df_jobs = pd.DataFrame(jobs_data)
        df_jobs = df_jobs.iloc[::2]
       



    display(df_jobs)

