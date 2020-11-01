import numpy as np
from datetime import date
import pandas as pd
from pprint import pprint
import requests
from bs4 import BeautifulSoup

dates = pd.date_range('20201101', periods=100)
data_frame = pd.DataFrame(None, index=dates,
                          columns=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                                   'eleven', 'twelve'])
today = date.today()

url = 'https://pogoda.interia.pl/prognoza-dlugoterminowa-szklarska-poreba,cId,34920'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

temps = []
temperatures = soup.find_all(class_="table-temps")
for temperature in temperatures:
    temps.append(temperature.text.strip().split('\n'))

for i in range(12):
    data_frame.iat[i, i] = temps[i]

print(data_frame.head())

data_frame.to_csv('/home/gabriel/Desktop/weather_conspiracy.csv')