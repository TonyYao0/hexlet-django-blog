from django.urls import path
from hexlet_django_blog.article.views import IndexView, ArticleFormCreateView
from hexlet_django_blog.article import views

urlpatterns = [
    # Маршрут для списка статей
    path("", IndexView.as_view(), name='article_list'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
    path("<str:tags>/<int:article_id>/", IndexView.as_view(), name='article'),
    

]