from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.


def index(request):
    response = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2024-04-27&sortBy=publishedAt&apiKey=209b70796c9e4fc082c39d05f423276e").json()
    articles = response.get('articles', [])
    return render(request, 'index.html', {'articles': articles})
