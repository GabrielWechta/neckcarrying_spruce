import numpy as np
from datetime import date, timedelta
import pandas as pd
from pprint import pprint
import requests
from bs4 import BeautifulSoup

today = date.today()
path_to_csv = "/home/gabriel/Desktop/weather_conspiracy.csv"
TWELVE_COLUMNS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                  'eleven', 'twelve']

try:
    data_frame = pd.read_csv(path_to_csv, index_col=0)

except FileNotFoundError:
    print("File at \'", path_to_csv, "\' couldn't be found. Creating new one...")

    # creating procedure #
    print(today)
    dates = pd.date_range(today, periods=100)
    data_frame = pd.DataFrame(None, index=dates,
                              columns=TWELVE_COLUMNS)

url = 'https://pogoda.interia.pl/prognoza-dlugoterminowa-szklarska-poreba,cId,34920'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

temps = []
temperatures = soup.find_all(class_="table-temps")
for temperature in temperatures:
    temps.append(temperature.text.strip().split('\n'))

next_twelve_days = pd.date_range(today, periods=12)
for i, (index, column) in enumerate(zip(next_twelve_days.date, TWELVE_COLUMNS)):
    data_frame.at[index, column] = temps[i]

print(data_frame.head())

data_frame.to_csv('/home/gabriel/Desktop/weather_conspiracy.csv')
