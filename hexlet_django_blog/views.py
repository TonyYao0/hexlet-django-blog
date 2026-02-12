from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.http import HttpResponse

class IndexView(TemplateView):
    template_name = "index.html"
    def get(self, request, *args, **kwargs):
        url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
        return HttpResponse(f"Вы находитесь на главной. Ссылка на статью: {url}")


class AboutView(TemplateView):
    template_name = "about.html"