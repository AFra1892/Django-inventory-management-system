from django.shortcuts import render
from .models import Article
# Create your views here.

def home_view(request):
    return render(request , "articles/home.html")


def articles_view(request):
    all_articles = Article.objects.all()
    context = {
        "articles": all_articles
    }
    return render(request , "articles/articles.html" , context=context)

def article_detail_view(request , id):
    identified_article = Article.objects.get(id = id)
    context = {
        "article": identified_article
    }
    return render(request , "articles/detail.html" , context=context)

def create_article_view(request):
    context = {}
    if request.POST:
        print(request.POST)
        title = request.POST.get("title")
        content =  request.POST.get("content")
        context["title"] = title
        context["content"] = content
        # print(title , content)
        submitted_article = Article(title=title , content=content)
        submitted_article.save()
        context["submited"] = True

    return render(request , "articles/create.html" , context=context)