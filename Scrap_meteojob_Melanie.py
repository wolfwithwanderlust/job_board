#Récupération des informations pertinente

import pandas as pd
import requests
from bs4 import BeautifulSoup

def extract_job_data(url):
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
        df_jobs = df_jobs.iloc[::1]
        return df_jobs
    else:
        return None

# Exemple d'utilisation de la fonction
url = "https://www.meteojob.com/jobs?what=data&where=Lyon"
df_jobs = extract_job_data(url)
if df_jobs is not None:
    display(df_jobs)
else:
    print("Une erreur s'est produite lors de la récupération des données.")

########################################################################################################################
#Dataframe trié par Lieu

import pandas as pd
import requests
from bs4 import BeautifulSoup

def extract_job_data(url):
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
        df_jobs = df_jobs.iloc[::1]
        return df_jobs
    else:
        return None

# Exemple d'utilisation de la fonction
url = "https://www.meteojob.com/jobs?what=data&where=Lyon"
df_jobs = extract_job_data(url)
if df_jobs is not None:
    # Créer un DataFrame par lieu
    df_jobs_by_location = df_jobs.groupby('Lieu').apply(lambda x: x.reset_index(drop=True))
    display(df_jobs_by_location)
else:
    print("Une erreur s'est produite lors de la récupération des données.")

########################################################################################################################
#Dataframe dédié à chaque Lieu

import pandas as pd
import requests
from bs4 import BeautifulSoup

def extract_job_data(url):
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
        df_jobs = df_jobs.iloc[::1]
        return df_jobs
    else:
        return None

# Exemple d'utilisation de la fonction
url = "https://www.meteojob.com/jobs?what=data&where=Lyon"
df_jobs = extract_job_data(url)
if df_jobs is not None:
    # Créer un DataFrame par lieu
    dfs_by_location = {}
    for location, group in df_jobs.groupby('Lieu'):
        dfs_by_location[location] = group.reset_index(drop=True)

    # Afficher les DataFrames par lieu
    for location, df in dfs_by_location.items():
        print(f"Emploi à {location}:")
        display(df)
else:
    print("Une erreur s'est produite lors de la récupération des données.")
