import csv
import tweepy
from tweepy import OAuthHandler
from datetime import datetime

#Twitter developer account credentials
consumer_key = "b1u6ewSssdeuWQ2pnELH7o5s0"
consumer_secret = "JEfXBZfkba62pPrfXzmyoZXFZcUNwG0xl7elb0ZLXuhoECVy3P"
access_token = "1308202512105779200-aEuy8Q1b6OIJ9ayMbTdNQkmqLK3kt6"
access_token_secret = "0SCWL59f4g6RozN2XbeENn8HfyNqgovs7QGsp6cKNnOSh"

#Authentication with Twitter
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#RECENT TITLES
news_sources_usernames = ["CNN", "nytimes", "CBSNews", "NBCNews"]

#Gets the recent timeline of a news source
def get_stories(username, number):
    stories = tweepy.Cursor(api.user_timeline, id=username).items(number)
    stories_list = [[username]]
    temp = [[story.text] for story in stories]
    return stories_list + temp

#Records the tweets and the original stories to a spreadsheet
def record_timeline(sources):
    all_stories = []
    filename = 't_article_titles.csv'
    for username in sources:
        all_stories.append(get_stories(username, 20))
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in all_stories:
            writer.writerow(["----------------"])
            writer.writerows((row))



#TRENDING TITLES
WOEID = 23424977

#Gets the trending tags in the US Twitter region
def get_trending():
    us_trending = []
    trending_tags = api.trends_place(id=WOEID)
    for value in trending_tags:
        for trend in value['trends']:
            us_trending.append(trend['name'])
    return us_trending

def add_trending_tags(us_trending):
    filename = 'r-t_trending_news.csv'
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([" "])
        writer.writerow(["Twitter"])
        writer.writerow(["----------------"])
        writer.writerow([datetime.now()])
        writer.writerow(["----------------"])
        for row in us_trending:
            writer.writerow([row])

if __name__ == '__main__':
    add_trending_tags(get_trending())
# if __name__ == '__main__':
#     record_timeline(news_sources_usernames)