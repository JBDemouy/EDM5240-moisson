#! python3
# coding: utf-8
# Martin Ouellet-Diotte

### Quelle idée originale!
### Script impeccable!
### Commentaires complets, incluant attribution de tes sources de documentation
### Une seule petite question sur une variable qui semble inutile

# À l'aide de l'API de Reddit, ce petit code permet de moissonner les données des sous-forums du site (subreddits)
# Dans ce cas-ci, compilation des 1000 publications les plus controversées du forum principal de nouvelles (r/News)
# Moissonage réalisé avec l'aide du tuto suivant: http://www.storybench.org/how-to-scrape-reddit-with-python/

import praw # Praw permet la connexion à l'API de Reddit, téléchargement externe. 
import csv
import datetime

fichier = "news.csv"
fichier = "news_JHR_quebec.csv" ### Nouveau fichier simplement pour vérifier de mon côté

Scrape = praw.Reddit(client_id='iamIWmkN5oxdCw', \
                     client_secret='OnH5LwgZIy7IVS_72ikq_VugRGE', \
                     user_agent='MoissonUQAM', \
                     username='scrapingforuqam', \
                     password='scrapescrapescrape') # Informations de connexion pour l'API.

sub = Scrape.subreddit('worldnews') # Sélection du sub, dans ce cas-ci `r/worldnews'.
sub = Scrape.subreddit('quebec') # Sélection du sub, dans ce cas-ci `r/worldnews'. ### J'essaie avec un autre
top_sub = sub.controversial() # Les publications dans 'r/worldnews' serons triées selon le taux de controverse (l'écart entre les votes positifs et négatifs).
### Tu fais quoi avec la variable «top_sub»??

for post in sub.controversial(limit=1000): # On ouvre ici la boucle et on détermine le nombre de publications extraites à 1000. 
	print(post)
	e = []
	e.append(post.title) # Le titre de la publication
	e.append(post.score) # Le score (nombre de vote positif)
	e.append(post.id) # ID reddit pour retrouver la publication
	e.append(post.url) # URL de la publication
	e.append(post.num_comments) # Nombre de commentaires
	e.append(datetime.datetime.utcfromtimestamp(post.created_utc)) # Date de création de la publication avec traduction du temps Unix
	print(e) # Impression pour le terminal
	print("_"*80)

	News = open(fichier, "a", encoding='utf-8') # L'encodage est publié ici pour contourner une erreur unicode. 
	td = csv.writer(News)
	td.writerow(e)

# On peut constater que les nouvelles concernant la Palestine et Israel sont particulièrement controversées, voir CSV dans le repo.
