# Twitter/Reddit News Scraper
Collects data from Twitter and Reddit to see the trending title tags and news stories

## Program Breakdowns:
### reddit_manual_scraper
- Uses BeautifulSoup instead of the Reddit API
- Takes the titles and the original stories links of the top four posts in the Reddit News section
- Not very effective, but is a good introduction to web-scraping
### twitter_recent_news
- Uses the Twitter API with a developer account
- Allows users to create a list of news accounts they trust and acquires the recent news posts on those accounts
- Records the top trending tags on Twitter, given a specified location id (WOEID)
- Effective, but lacks the updating the list of new posts, cannot access the Explore News section of Twitter
