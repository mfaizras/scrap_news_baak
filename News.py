from typing import Optional
import requests as r
from bs4 import BeautifulSoup
from datetime import datetime

class News:

    def __init__(self, title:str = None, url:str = None, body:str = None, date:str = None) -> None:
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
                self.title = article_data.find('h6').find('a').text
                self.url = article_data.find('h6').find('a')['href']
                self.body = article_data.find(class_='offset-top-5').find('p').text
                self.date = article_data.find('span', class_="text-middle inset-left-10 text-italic text-black").text
                article_lists.append(self)
            return article_lists
        else:
            return None
        
    def get_data_filter_by_day(self) -> list['News'] | None:
        results = self.get_data_news()
        for result in results:
            date_format = "%d/%m/%Y"
            formatted_date = datetime.strptime(result.date, date_format)
        
            if formatted_date >= datetime.now():
                print(formatted_date)
            else:
                print("no news already")
    
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
            return ValueError("News not found")