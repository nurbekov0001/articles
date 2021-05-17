from django.urls import path

from article.views import (
    IndexView,
    ArticleView,
    CreateArticleView,
    ArticleUpdateView,
    ArticleCommentCreate,
    ArticleDeleteView
)
from article.views.articles import LikeArticle, UnLikeArticle
from article.views.comments import LikeComment, UnLikeComment

app_name = 'article'

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
    path('add/', CreateArticleView.as_view(), name='add'),
    path('<int:pk>/', ArticleView.as_view(), name='view'),
    path('<int:pk>/update', ArticleUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='delete'),
    path('<int:pk>/comments/add/', ArticleCommentCreate.as_view(), name='comment_create'),
    path('<int:pk>/like', LikeArticle.as_view(), name='article_like'),
    path('<int:pk>/unlike', UnLikeArticle.as_view(), name='article_unlike'),
    path('<int:pk>/comment/like', LikeComment.as_view(), name='comment_like'),
    path('<int:pk>/comment/unlike', UnLikeComment.as_view(), name='comment_unlike'),
]
