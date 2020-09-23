import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

headers ={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"}
url = "https://www.reddit.com/r/news/"
r = requests.get(url, headers=headers)
news_titles = []
orig_stories = []


#Takes the post titles and the links to the original stories in the Reddit News tab
def news_articles():
    soup = BeautifulSoup(r.text, 'html5lib')

    titles = soup.findAll('h3', {'class': '_eYtD2XCVieq6emjKBH3m'})
    links = soup.findAll('a', {'class':'_13svhQIUZqD9PVzFcLwOKT styled-outbound-link'})

    for title in titles:
        title = title.get_text()
        news_titles.append([title])
    for link in links:
        link = link['href']
        orig_stories.append([link])

#Stores the taken information into a spreadsheet for tracking each day
def stories_spreadsheet(a, b):
    filename = 'news_titles.csv'
    rows = zip(b, a)
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Reddit"])
        writer.writerow(["----------------"])
        writer.writerow([datetime.now()])
        writer.writerow(["----------------"])
        for row in rows:
            writer.writerow(row)


if __name__ == '__main__':
    news_articles()
    stories_spreadsheet(news_titles, orig_stories)