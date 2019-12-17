from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


match = soup.title.text
print(match)

#paragraph tag 
para = soup.p
print(para)

#Using a find() to search for a specific paragraph
div = soup.find('div', class_='footer')
print(div)
article = soup.find('div', class_='article')
print(article)

#searching within a setence
headline = article.a.h2.text
# print(headline)

summary = article.p.text
print(summary )

#Getting multiple things from a page using the find or method
for article in soup.find_all('div', class_='article'):
    headline = article.a.h2.text
    print(headline)

    summary = article.p.text
    print(summary)

    print() #creates a blank line within our articles

