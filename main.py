from datetime import date

import pandas as pd
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

temperatures = soup.find_all(class_="table-temps")
temps = [temp.text.strip().split('\n') for temp in temperatures]

next_twelve_days = pd.date_range(today, periods=12)
for i, (index, column) in enumerate(zip(next_twelve_days.date, TWELVE_COLUMNS)):
    data_frame.at[str(index), column] = temps[i]

print(data_frame.head())

data_frame.to_csv('/home/gabriel/Desktop/weather_conspiracy.csv')
