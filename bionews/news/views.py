from django.shortcuts import render
import requests
from .models import NewsArticle

def index(request):
    api_key = '9fce8f78bb684c3380c5d8e067a95899'
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey={api_key}&q=biotechnology'
    response = requests.get(url)
    articles = response.json()['articles']

    for article in articles:
        title = article['title']
        author = article['author']
        description = article['description']
        url = article['url']
        url_to_image = article['urlToImage']
        published_at = article['publishedAt']

        NewsArticle.objects.create(
            title=title,
            author=author,
            description=description,
            url=url,
            url_to_image=url_to_image,
            published_at=published_at
        )

    return render(request, 'news/index.html', {'articles': articles})

