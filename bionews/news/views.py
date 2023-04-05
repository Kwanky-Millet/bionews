from django.shortcuts import render
import requests

def index(request):
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=us&category=science&'
           'apiKey=9fce8f78bb684c3380c5d8e067a95899'
    )
    response = requests.get(url)
    articles = response.json()['articles']
    return render(request, 'news/index.html', {'articles': articles})

