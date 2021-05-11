from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializer import ArticleSerializer
from .models import Article

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all().order_by("created_at")

    def get_queryset(self):
        return self.queryset
