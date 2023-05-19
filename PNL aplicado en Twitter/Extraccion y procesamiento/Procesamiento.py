import pandas as pd
import pickle

with open('dic_tw.pkl', 'rb') as archivo:
    # Cargar el objeto almacenado en el archivo
    objeto_cargado = pickle.load(archivo)
    
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)
 
for i in objeto_cargado.keys():
    objeto_cargado[i] = (objeto_cargado[i].Tweet.apply(preprocess)).to_frame()
    
with open("tweets_procesados.pkl", "wb") as tf:
    pickle.dump(objeto_cargado, tf)
