from scrape import data_list
import pandas as pd

df = pd.DataFrame(data_list)
df.set_index('SIF', inplace=True)

df.to_csv('dados_mapa.csv', index=True)