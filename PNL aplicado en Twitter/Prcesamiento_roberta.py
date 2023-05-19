from transformers import pipeline
import pickle

roberta = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
procesar = pipeline("sentiment-analysis", model=roberta, tokenizer=roberta)

with open('tweets_procesados.pkl', 'rb') as f:
    tweets = pickle.load(f)
 
# rdo = procesar("Buen dia")
# rdo[0]['label']

def procesar_tw(texto):
  rdo = procesar(texto)
  return rdo[0]['label']

for i in tweets.keys():
  tweets[str(i)]['Sentimiento'] = tweets[str(i)].Tweet.apply(procesar_tw)
  print("Proceso:", i)
  
with open('tweets.pickle', 'wb') as archivo:
  pickle.dump(tweets, archivo)
