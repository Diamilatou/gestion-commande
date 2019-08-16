#coding:utf-8
from flask import Flask
app = Flask(__name__)
import feedparser

url=["https://guineeinnovations.com/feed/","https://www.jeuneafrique.com/rss","https://blog.futuresfestivals.com/feed/",
"https://startupbrics.com/feed/","https://www.afrikatech.com/fr/feed/","https://www.coinafrique.com/feed/"]


for u in url:
	page=feedparser.parse(u)
	print(u)           
	for post in page.entries:
		lien=post.link
		titre=post.title
		print(titre+":"+lien )
		 






"""a=page.entries[1]
b=a.title
print(b)  
if titre and lien in ('innovation','innovations africaines','afrique innovation','afrique'):
			print("les innovations africaines")"""