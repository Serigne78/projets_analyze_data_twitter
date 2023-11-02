import json
import re
import pandas as pd
import textblob

df = pd.read_json("aitweets.json")



# Assurez-vous d'avoir déjà chargé vos données dans un DataFrame, par exemple, df.

def topk_hashtag(k):
    hashtags_freq = {}  # Dictionnaire pour stocker la fréquence des hashtags

    for tweet_text in df["TweetText"]:
        hashtags = re.findall(r'#\w+', tweet_text)  # Trouver tous les hashtags dans le texte
        for hashtag in hashtags:
            hashtag = hashtag.lower()  # Convertir en minuscules pour compter de manière insensible à la casse
            if hashtag in hashtags_freq:
                hashtags_freq[hashtag] += 1
            else:
                hashtags_freq[hashtag] = 1

    # Trier les hashtags par fréquence décroissante
    sorted_hashtags = sorted(hashtags_freq.items(), key=lambda x: x[1], reverse=True)

    # Afficher les k hashtags les plus courants
    top_k_hashtags = sorted_hashtags[:k]
    for hashtag, count in top_k_hashtags:
        print(f"Hashtag : {hashtag}, Fréquence : {count}")

# Exemple d'utilisation pour afficher les 5 hashtags les plus courants
topk_hashtag(int(input("Top K hastags: ")))

def extraction_hashtags(id):
    tweet_recherche = df.loc[df['id'] == id]
    texte_du_tweet = tweet_recherche['TweetText'].values[0]
    pattern = r'#\w+'
    print(texte_du_tweet)
    print(re.findall(pattern, texte_du_tweet))
extraction_hashtags(1415291947560828928)

def extraction_user(id):
    tweet_recherche = df.loc[df['id'] == id]
    texte_du_tweet = tweet_recherche['TweetText'].values[0]
    pattern = r'@\w+'
    print(texte_du_tweet)
    liste = re.findall(pattern, texte_du_tweet)
    return liste
extraction_user(1415291947560828928)

def find_user_mention(mention):
    for tweet in df["TweetText"]:
        if mention in tweet:
            print(mention)
            print(tweet)
find_user_mention("@jason_lazer")


def find_user_hashtags(hashtag):
    for tweet in df["TweetText"]:
        if hashtag in tweet:
            print(hashtag)
            print(tweet)
find_user_mention("#hdatasystems")


def sentiment(id):
    s = df.loc[df['id'] == id]
    texte= s['TweetText']
    texte=str(texte)
    blob =TextBlob(texte)
    sentiment = blob.sentiment
    r=sentiment.polarity
    if r<=0:
        return ':('
    else:
        return ':)'

print(sentiment(1415291877897605120))
     



    
