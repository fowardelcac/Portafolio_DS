import pandas as pd
import snscrape.modules.twitter as st
import re

usuarios = ['@JMilei', '@alferdez', '@CFKArgentina', '@PatoBullrich', '@horaciorlarreta']

def crear_df(lista):
    return pd.DataFrame(lista, columns=['Date', 'Tweet'])

def get_tweets(palabra_clave, usuario):
    lista = []
    for tw in st.TwitterSearchScraper(palabra_clave).get_items():
        text = tw.rawContent
        menciones = re.findall(r"@\w+", text)
        menciones_filtradas = [mencion for mencion in menciones if mencion != usuario]
        if len(menciones_filtradas) == 0:
          lista.append([tw.date, text])
    
    return crear_df(lista)

dic_tw = {}
for i in usuarios:
    ii = str(i)
    key = (f'({i}) since:2022-04-13')
    dic_tw[i] = get_tweets(key, i)
    print('Recibido: ', i)
