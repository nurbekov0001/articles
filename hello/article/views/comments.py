from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import JsonResponse, HttpResponseForbidden
from django.views.generic import CreateView
from django.shortcuts import reverse, get_object_or_404
from django.views.generic.base import View

from article.forms import CommentForm
from article.models import Comment, Article, Intermediate_table_of_cometaries_and_users


class ArticleCommentCreate(PermissionRequiredMixin, CreateView):
    template_name = 'comments/create.html'
    form_class = CommentForm
    model = Comment
    permission_required = 'article.add_comment'

    def get_success_url(self):
        return reverse(
            'article:view',
            kwargs={'pk': self.kwargs.get('pk')}
        )
    
    def form_valid(self, form):
        article = get_object_or_404(Article, id=self.kwargs.get('pk'))

        comment = form.instance
        comment.article = article
        comment.author = self.request.user

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Intermediate_table_of_cometaries_and_users.objects.filter(user=self.request.user)
        comments_id = []
        for coment in comments:
            comments_id.append(coment.comment.pk)
        context['comments_likes'] = comments_id
        return context




class LikeComment(View):
    def get(self, request, *args, **kwargs):
        coment = get_object_or_404(Comment, pk=kwargs['pk'])
        like = coment.like_comments.filter(user=request.user)
        if not like:
            Intermediate_table_of_cometaries_and_users.objects.create(user=request.user, comment=coment)
            return JsonResponse({'count': coment.like_comments.count()})
        else:
            return HttpResponseForbidden('Лайк уже поставлен', status=403)


class UnLikeComment(View):
    def get(self, request, *args, **kwargs):
        coment = get_object_or_404(Comment, pk=kwargs['pk'])
        like = coment.like_comments.filter(user=request.user)
        if like.exists():
            like.delete()
            return JsonResponse({'count': coment.like_comments.count()})
        else:
            return HttpResponseForbidden('Лайк не был поставлен', status=403)

