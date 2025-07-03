from django.urls import path 
from .views import (NewsList, NewsDetail, NewsCreate, NewsUpdate, NewsDelete, ArticleCreate, NewsSearch)

urlpatterns = [ 
    path('', NewsList.as_view(), name='news_list'), 
    path('search/', NewsSearch.as_view(), name='news_search'), 
    path('create/', NewsCreate.as_view(), name='news_create'), 
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail'), 
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'), 
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'), 
    path('articles/create/', ArticleCreate.as_view(), name='article_create'), 
    path('articles/<int:pk>/edit/', NewsUpdate.as_view(), name='article_edit'), 
    path('articles/<int:pk>/delete/', NewsDelete.as_view(), name='article_delete'), 
    ]