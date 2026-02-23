from django.urls import path
from hexlet_django_blog.article.views import IndexView
from hexlet_django_blog.article import views

urlpatterns = [
    # Маршрут для списка статей
    path("", IndexView.as_view(), name='article_list'),
    
    # Маршрут, который ищет reverse на главной странице
    # ВАЖНО: имена параметров должны совпадать с тем, что в reverse (tags и article_id)
    path("<str:tags>/<int:article_id>/", IndexView.as_view(), name='article'),
]