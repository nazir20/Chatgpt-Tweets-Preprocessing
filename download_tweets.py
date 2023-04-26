# Packages
import snscrape.modules.twitter as sntwitter
import pandas as pd

# from google.colab import drive
# drive.mount('/content/drive')

query= '(#chatgpt) lang:en until:2023-03-19 since:2022-11-01'
tweets=[]
limit=30000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    if len(tweets)==limit:
        break
    else:
        tweets.append([tweet.date,tweet.user.username,tweet.content])

        
df= pd.DataFrame(tweets, columns=['Date','User','Tweet'])
# save tweets inside a csv file
df.to_csv('chatgpt_tweets.csv')
