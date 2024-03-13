# Fonction scraping with scroll
import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_job_listings(url, pages):
    jobs_data = []
    
    for i in range(2, pages + 5):
        scroll_url = f"{url}&page={i}"
        response = requests.get(scroll_url)
        
        if response.status_code == 200:
            htmlData = response.content
            soup = BeautifulSoup(htmlData, 'html.parser')
            job_listings = soup.find_all('div', class_='truncated-text-fix')

            for job in job_listings:
                title = job.find('h2').text.strip() if job.find('h2') else ''
                company = job.find(class_="d-inline-block mt-1 mb-0 ng-star-inserted").text.strip() if job.find(class_="d-inline-block mt-1 mb-0 ng-star-inserted") else ''
                types = job.find(class_="mr-1 mb-0 ng-star-inserted").text.strip() if job.find(class_="mr-1 mb-0 ng-star-inserted") else ''
                date = job.find(class_="cc-font-size-small").text.strip() if job.find(class_="cc-font-size-small") else ''
                salary = job.find(class_="cc-tag-primary-light").text.strip() if job.find(class_="cc-tag-primary-light") else ''
                jobs_data.append({"Titre": title,"Company": company,"Type_de_contrat": types,"date_de_publication":date,"salaire" :salary})

    df_jobs = pd.DataFrame(jobs_data)
    display(df_jobs)

# Utilisation de la fonction
url = "https://www.meteojob.com/jobs?what=Data&where=Lyon"
scrape_job_listings(url, pages=5)  # Scrapes job listings de la pages 2 à 5

# Fonction récupérer que les offres avec salaires

# Importation des librairies
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Définition de l'url à scraper
url = "https://www.meteojob.com/jobs?what=Data&where=Lyon"

# initialistion de la table vide
jobs_data = []

# Définition du nombre de pages à scraper
num_pages = 6

# boucle for qui vas faire chaque page
for i in range(1, num_pages + 1):
    # Construction de l'url pour le scrolling
    scroll_url = f"{url}&page={i}"
    
    # envoyer une requète GET à URL
    response = requests.get(scroll_url)
    
    # férification du succés de la requète
    if response.status_code == 200:
        # Extraction du contenue HTML
        htmlData = response.content
        
        # Parser le contenu HTML en utiloisant BeautifulSoup
        soup = BeautifulSoup(htmlData, 'html.parser')
        
        # Trouver la liste des offres
        job_listings = soup.find_all('div', class_='truncated-text-fix')
        
        # boucle pour récupérer chaque information sur chaque page
        for job in job_listings:
            # Extraction des détail de l'offre
            title = job.find('h2').text.strip() if job.find('h2') else ''
            company = job.find(class_="d-inline-block mt-1 mb-0 ng-star-inserted").text.strip() if job.find(class_="d-inline-block mt-1 mb-0 ng-star-inserted") else ''
            types = job.find(class_="mr-1 mb-0 ng-star-inserted").text.strip() if job.find(class_="mr-1 mb-0 ng-star-inserted") else ''
            date = job.find(class_="cc-font-size-small").text.strip() if job.find(class_="cc-font-size-small") else ''
            salary = job.find(class_="cc-tag-primary-light").text.strip() if job.find(class_="cc-tag-primary-light") else ''
            
            # Vérification de la cellule Salary 
            if salary:
                # Ajouter les offres aves la cellule salaire remplie 
                jobs_data.append({"Titre": title, "Company": company, "Type_de_contrat": types, "date_de_publication": date, "salaire": salary})
    else:
        print(f"Failed to retrieve data from page {i}.")

# Create a DataFrame from the job data list
df_jobs = pd.DataFrame(jobs_data)

# Display the DataFrame
display(df_jobs)
