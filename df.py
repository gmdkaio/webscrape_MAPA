from scrape import data_list
import pandas as pd

df = pd.DataFrame(data_list)
df.set_index('SIF', inplace=True)
df = df.drop('Unnamed: 0', axis=1)

df.to_csv('dados_mapa.csv', index=True)