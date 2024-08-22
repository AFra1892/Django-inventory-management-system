from django.urls import path
from . import views
urlpatterns = [
    path("" , views.home_view , name="home_view"),
    path("articles/" , views.articles_view , name = "article_view"),
    path("articles/<int:id>" , views.article_detail_view , name="article_detail_view"),
    path("articles/create" , views.create_article_view , name = "create_article_view"),
    # path("articles/search/<int:id>" , views.search_article_view , name = "search_article_view")
]
