from bs4 import BeautifulSoup
import requests
 
#Getting source code from a website using requests library
source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    # Searching for a div with a specific class(entry-content)
    summary = article.find('div', class_='entry-content').p.text
    print(summary)  

    try:
        vid_src = article.find('iframe')['src']

        # split()- splits a string with list of values specified
        #searching for the video id
        vid_id = vid_src.split('/')[4]
        vid_id = vid_src.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
       yt_link = None

    print(yt_link)

    print()  

