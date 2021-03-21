#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author : yangge.yw
# @Time : 2021/2/12 1:39 下午
# @File : newspaperDemo.py
# @desc : newspaperDemo使用指南

import newspaper
from newspaper import Article
from newspaper import fulltext
import requests
url = 'https://www.wired.com/'

paper = newspaper.build(url, language="en", memoize_articles=False)

# for article in paper.articles:
#     print(article.url)
# print(paper)

# for category in paper.category_urls():
#     print(category)


# article = Article('https://www.wired.com/story/preterm-babies-lonely-terror-of-a-pandemic-nicu/')
# article.download()
# article.parse()
# print("title=", article.title)
# print("author=", article.authors)
# print("publish_date=", article.publish_date)
# print("top_image=", article.top_image)
# print("movies=", article.movies)
# print("text=", article.text)
# print("summary=", article.summary)

# first_url = paper.articles[0]
# first_url.download()
# first_url.parse()
# print(first_url.title)
# print(first_url.publish_date)
# print(first_url.authors)
# print(first_url.top_image)
# print(first_url.summary)
# print(first_url.movies)
# print(first_url.text)


# html = requests.get('https://www.wired.com/story/preterm-babies-lonely-terror-of-a-pandemic-nicu/').text
# print('获取的原信息-->', html)
# text = fulltext(html, language='en')
# print('解析后的信息', text)

# first_article = paper.articles[1]
# first_article.download()
# first_article.parse()
# first_article.nlp()
# print(first_article.summary)
# print(first_article.keywords)


print(newspaper.hot())
print(newspaper.popular_urls())

