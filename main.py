import logging
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


headers = {'Accept-Language': 'en-US, en;q=0.5'}
url = 'https://www.imdb.com/search/title/?groups=top_1000&ref_adv_prv'
results = requests.get(url, headers=headers)
soup = BeautifulSoup(results.text, 'html.parser')
print(soup.prettify())

# empty list
titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []



