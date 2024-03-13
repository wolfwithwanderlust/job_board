#Stockage des données

import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

url = "https://www.meteojob.com/jobs?what=data&where=Lyon"
response = requests.get(url)
if response.status_code == 200:
    htmlData = response.content
    soup = BeautifulSoup(htmlData, 'html.parser')

    job_listings = soup.find_all('div', class_='truncated-text-fix')
    jobsdata = []
    for job in job_listings:
        title = job.find('h2').text.strip() if job.find('h2') else ''
        company = job.find(class_="d-inline-block mt-1 mb-0 ng-star-inserted").text.strip() if job.find(class_="d-inline-block mt-1 mb-0 ng-star-inserted") else ''
        types = job.find(class_="mr-1 mb-0 ng-star-inserted").text.strip() if job.find(class_="mr-1 mb-0 ng-star-inserted") else ''
        localisation = job.find(class_="mr-3 mb-1 cc-font-size-small mb-lg-3 mr-lg-0").text.strip() if job.find(class_="mr-3 mb-1 cc-font-size-small mb-lg-3 mr-lg-0") else ''
        date = job.find(class_="cc-font-size-small").text.strip() if job.find(class_="cc-font-size-small") else ''
        salaire = job.find(class_="cc-tag-primary-light").text.strip() if job.find(class_="cc-tag-primary-light") else ''

        jobsdata.append({"Titre de l'offre": title,"Société": company, "Lieu": localisation, "Type d'offre": types, "Date d'actualisation": date,
                         "Salaires": salaire})
    df_jobs = pd.DataFrame(jobsdata)
    df_jobs.to_csv('jobs.csv', index=False)  # Cette ligne ajoute l'exportation au format CSV

display(df_jobs)
