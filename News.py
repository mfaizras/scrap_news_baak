from typing import Optional
import requests as r
from bs4 import BeautifulSoup
from datetime import datetime

class News:

    def __init__(self, id:int = None, title:str = None, url:str = None, body:str = None, date:str = None) -> None:
        self.id = id
        self.title = title
        self.url = url
        self.body = body
        self.date = date

    def get_data_news(self) -> list['News'] | None:
        response = r.get("https://baak.gunadarma.ac.id/berita")
        if response.status_code == 200:
            article_lists = []
            sp = BeautifulSoup(response.content, 'html.parser')
            article_lists_scrap = sp.find_all('div', class_='post-news-body')
            for article_data in article_lists_scrap:
                h6 = article_data.find('h6')
                self.title = h6.find('a').text
                self.url = h6.find('a')['href']
                self.id = self.url.split("/")[-1]
                self.body = article_data.find(class_='offset-top-5').find('p').text
                self.date = article_data.find('span', class_="text-middle inset-left-10 text-italic text-black").text
                article_lists.append(News(
                    self.id,
                    self.title,
                    self.url,
                    self.body,
                    self.date
                ))
            return article_lists
        else:
            return None
        
    def get_data_filter_by_day(self) -> list['News'] | None:
        results = self.get_data_news()

        news = []
        for result in results:
            date_formatted = datetime.strptime(result.date, "%d/%m/%Y")
            if date_formatted <= datetime.now():
                news.append(result)

        return news
    
    def get_new_by_id(self, id:int) -> Optional['News'] | ValueError:
        url = f"https://baak.gunadarma.ac.id/berita/{id}"
        response = r.get(url)
        
        if response.status_code == 200:
            sp = BeautifulSoup(response.content, 'html.parser')
            news = sp.find('div', class_="cell-sm-8 cell-md-8 text-left")
            self.title = news.find('h3', class_='text-bold').text
            body = news.find_all_next(class_='offset-md-top-20')
            self.url = url
            self.date = body[0].find_all_next('ul')[0].find_all_next('li')[0].text
            self.body = body[1].text
            return self
        else:
            return ValueError("News ID not found")