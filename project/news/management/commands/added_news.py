import requests
from bs4 import BeautifulSoup
from django.core.management import BaseCommand

from news.models import News


class NewsParser:
    def get_news(self):
        url = 'https://news.ycombinator.com'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        items = soup.find_all('tr', class_='athing')
        for item in items[:30]:
            n = News(
                title=item.find('a', class_='storylink').get_text(strip=True),
                url=item.find('a', class_='storylink').get('href'),
            ).save()


class Command(BaseCommand):
    help = 'Added new from "Hacker News"'

    def handle(self, *args, **options):
        n = NewsParser()
        n.get_news()
