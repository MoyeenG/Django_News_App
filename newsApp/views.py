from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.

def index(request):
    newsApi = NewsApiClient(api_key='3a7a83b0f45645dd8df44905ca9abf7e')
    headlines = newsApi.get_top_headlines(sources='al-jazeera-english')
    articles = headlines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    mylist = list(zip(news, desc, img))

    return render(request, "newsApp/index.html", context={"mylist": mylist})
