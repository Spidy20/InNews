from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from newspaper import Article
import nltk

nltk.download('punkt')

# By major topics
# https://news.google.com/news/rss/headlines/section/TOPIC/SPORTS

# Top news
# https://news.google.com/news/rss

# By Search query
# https://news.google.com/rss/search?q={query}

site = 'https://news.google.com/rss/search?q=politics'
op = urlopen(site)  # Open that site
rd = op.read()  # read data from site
op.close()  # close the object
sp_page = soup(rd, 'xml')  # scrapping data from site
news_list = sp_page.find_all('item')  # finding news
print(news_list)
for news in news_list:  # printing news
    print('Title: ',news.title.text)
    print('News Link ',news.link.text)
    news_data = Article(news.link.text)
    news_data.download()
    news_data.parse()
    news_data.nlp()
    print("News Summary: ",news_data.summary)
    print("News Poster Link: ",news_data.top_image)
    print("Pub date: ",news.pubDate.text)
    print('-' * 60)
