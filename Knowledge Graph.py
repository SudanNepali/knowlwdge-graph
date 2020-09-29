from bs4 import BeautifulSoup
import requests
import re
import string
"""Scrapping Text from onlinekhabar"""
html=requests.get('https://english.onlinekhabar.com/things-not-to-do-while-trekking-in-nepali-himalayas.html').content
unicode_str = html.decode("utf8")
encoded_str = unicode_str.encode("ascii",'ignore')
news_soup = BeautifulSoup(encoded_str, "html.parser")
a_text = news_soup.find_all('p')
scrapped_text=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
scrapped=str(scrapped_text)

#print(scrapped_text)
"""Cleaning the text for further operations using"""
import spacy
nlp=spacy.load("en_core_web_sm")
doc=nlp(scrapped)
for tok in doc.sents:
    print(tok.text)

