
from django.urls import path, include

from api_v2.views import ArticleView, Article

app_name = 'api_v2'


article_urls = [
    path('', ArticleView.as_view(), name='articles'),
    path('<int:pk>/', Article.as_view()),
]


urlpatterns = [
    path('articles/', include(article_urls)),
]