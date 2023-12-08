import requests as r
from bs4 import BeautifulSoup

class News:
    def __init__(self, title, link, content):
        self.title = title
        self.link = link
        self.content = content

def main():
    result = scrap_data_news()
    print(result)

   
def scrap_data_news() -> News | None:
    response = r.get("https://baak.gunadarma.ac.id/berita")
    
    if response.status_code == 200:
        sp = BeautifulSoup(response.content, 'html.parser')

        article_lists = sp.find_all('div', class_='post-news-body')
        
        article_lists = []  # Initialize an empty list to store article data
        for article_data in sp.find_all('article', class_='post-news'):
            title = article_data.find('h6').find('a').text
            url = article_data.find('h6').find('a')['href']
            content = article_data.find(class_='offset-top-5').find('p').text
            
            data = News(title, url, content)
            article_lists.append(data)
        return article_lists
    else:
        return None

main()