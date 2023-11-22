import json
import re
import pandas as pd
import textblob
import matplotlib.pyplot as plt
import random
from gensim import corpora, models
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim.parsing.preprocessing import preprocess_string
from langdetect import detect


"""
with open("aitweets.json", "r", encoding="utf-8") as f:
    tweets = json.load(f)

auteur = ["TwitMaster23",
    "Tweetophile",
    "CoeurDeTweeter",
    "ChroniqueurTweets",
    "FlècheDeTweet",
    "Pionnel Pessi",
    "Leize.py",
    "ÉchoTweeter",
    "Dimitri.lasdeg",
    "PixelTweeter",
    "Yanis180",
    "NuageDeMots",
    "RésonanceTwitter",
    "HarmonieDeTweets",
    "ÉclatDePlume",
    "TempêteDeMots",
    "FusionTweets",
    "CascadeDeTweets",
    "PoésieDePixels",
    "ZénithTweeter",
    "ÉclipseDeMots",
    "AstreDeTweets",
    "SymphonieTwitter",
    "LueurDePlume",
    "VirtuoseDeTweets",
    "SillageDeMots",
    "PépiteTweeter",
    "OrageDeTweets",
    "PapillonDeMots",
    "RhapsodieTwitter",
    "MirageDeTweets",
    "EssenceDePlume",
    "OndeTweeter",
    "CascadeDeMots",
    "BrumeDeTweets",
    "MélopéeTwitter",
    "ÉclatDeTweeter",
    "EncreDeMots",
    "FlammeDeTweets",
    "TrésorDePlume",
    "AuroreTweeter",
    "MystèreDeMots",
    "LumièreTwitter",
    "RivièreDeTweets",
    "VagueDePlume",
    "ÉtoileTweeter",
    "ÉnigmeDeTweets",
    "BrisDeMots",
    "InspirationTwitter",
    "SoleilDeTweets",
    "LabyrintheDePlume",
    "RefletTweeter",
    "OasisDeMots",
    "ÉphémèreTwitter",
    "CristalDeTweets",
    "PassionDePlume",
    "RafaleTweeter",
    "CharmeDeMots",
    "ÉclipsTwitter",
    "CâlinDeTweets",
    "ÉmeraudeDePlume",
    "ÉchoTweeter",
    "AileDeMots",
    "LibelluleTwitter",
    "CaresseDeTweets",
    "SérénitéDePlume",
    "ÉtoileFilanteTweeter",
    "SongeDeMots",
    "ÉveilTwitter",
    "GazouillisDeTweets",
    "DouceurDePlume",
    "TempêteTweeter",
    "ÉvasionDeMots",
    "LueurTwitter",
    "ArcEnCielDeTweets",
    "InspirationDePlume",
    "RafaleTwitter",
    "OdysséeDeMots",
    "ÉclatTwitter",
    "GoutteDeTweets",
    "MerveilleDePlume",
    "OrageTwitter",
    "RêveDeMots",
    "HorizonDeTweets",
    "VibrationDePlume",
    "BriseTwitter",
    "MélodieDeTweets",
    "SérénadeDePlume",
    "CascadeTwitter",
    "ÉlixirDeMots",
    "RécitDeTweeter",
    "AubeTwitter",
    "EssenceDePlume",
    "ÉchoDeMots",
    "SouffleTweeter",
    "LueurDePlume",
    "ÉpisodeTwitter",
    "NuageDeMots",
    "InspirationDeTweeter",
    "VortexTwitter"
    ]
def supprimer_caracteres_speciaux(texte):
    # Utiliser une expression régulière pour supprimer les caractères spéciaux
    texte_propre = re.sub(r'[^\w\s@#]', '', texte)
    return texte_propre


for tweet in tweets:
    tweet["Author"] = random.choice(auteur)
    tweet["TweetText"] = supprimer_caracteres_speciaux(tweet["TweetText"])

with open('zone_atterissage.json', 'w', encoding='utf-8') as f:
    json.dump(tweets, f, ensure_ascii=False, indent=2)
"""
# Assurez-vous d'avoir déjà chargé vos données dans un DataFrame, par exemple, df.
df = pd.read_json("aitweets.json")
def topk_hashtag(k):
    hashtags_freq = {}  # Dictionnaire pour stocker la fréquence des hashtags

    for tweet_text in df["TweetText"]:
        hashtags = re.findall(r'#\w+', tweet_text)  # Trouver tous les hashtags dans le texte
        for hashtag in hashtags:
            # Convertir en minuscules pour compter de manière insensible à la casse
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


def topKmentionne(k):
    dic={}
    for tweet in df["TweetText"]:
        arobases = re.findall(r'@\w+', tweet)
        for arobase in arobases:
              # Convertir en minuscules pour compter de manière insensible à la casse
            if arobase in dic:
                dic[arobase] += 1
            else:
                dic[arobase] = 1
    sorted_arobases = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    top_k_arobases = sorted_arobases[:k]
    for arobase, count in top_k_arobases:
        print(f"Hashtag : {arobase}, Fréquence : {count}")

print(topKmentionne(int(input("Top K arobase: "))))


def topk_utilisateur(k):
    dico={}
    p=[]
    for auteur in df["Author"]:
        if auteur in dico:
            dico[auteur]+=1
        else:
            dico[auteur]=1
    maxi=0
    for j in range(k):
        for i in dico:
            if dico[i]>maxi:
                maxi=dico[i]
        p.append(i)
        del dico[i]
    return p


print(topk_utilisateur(int(input("Top K utilisateur: "))))

def nb_pub_par_user(auteur):
    s=0
    for i in df["Author"]:
        if auteur==i:
            s=s+1
    return s


print(nb_pub_par_user(str(input("user: "))))




    


    
