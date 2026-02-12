from django.urls import path
from hexlet_django_blog.article.views import ArticleIndexView
from hexlet_django_blog.article import views

urlpatterns =[
    path("", ArticleIndexView.as_view(), name='article_list'),
    path("<str:tags>/<int:article_id>/", ArticleIndexView.as_view(), name="article"),
]