
import json

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from article.models import Article
from api_v2.serializers import ArticleSerializer


class ArticleView(APIView):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        response_data = serializer.data

        return Response(data=response_data)

    def post(self, request, *args, **kwargs):
        article_data = request.data
        serializer = ArticleSerializer(data=article_data)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        return JsonResponse({'id': article.id})

class Article (APIView):
    def get(self, request, *args, **kwargs):
        try:
            article = Article.objects.get(pk=kwargs.get("pk"))
            article_srlz = ArticleSerializer(article)
            response_data = article_srlz.data
            return Response(response_data)
        except Article.DoesNotExist:
            return Response(data={"error": "error"}, status=404)

    def put (self, request, pk, *args, **kwargs):
        try:
            article = Article.objects.get(pk=pk)
            data = request.data
            update = ArticleSerializer(instance=article, data=dat
            if update.is_valid(raise_exception=True):
                update.save()
            return Response(data=update.data)
        except Article.DoesNotExist:
            return Response(data={"error": "error"}, status=404)


    def delete(self, request, pk, *args, **kwargs):
        try:
            article = Article.objects.get(pk=pk)
            article.delete()
            return Response()
        except Article.DoesNotExist:
            return Response(data={"error": "error"}, status=404)

