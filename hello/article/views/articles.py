from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode
from django.views.generic.base import View

from article.models import Article, Articles_and_users_intermediate_table
from article.forms import ArticleForm, SearchForm


class IndexView(ListView):
    """
    Представление для просмотра списка статей. Представление реализовано с
    использованием generic-представления ListView.

    В представлении активирована пагинация и реализован поиск
    """
    template_name = 'articles/index.html'
    model = Article
    context_object_name = 'articles'
    ordering = ('title', '-created_at')
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(IndexView, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(title__icontains=self.search_data) |
                Q(author__icontains=self.search_data) |
                Q(content__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form
        sss = Articles_and_users_intermediate_table.objects.filter(user=self.request.user)
        articles_id = []
        for s in sss:
            articles_id.append(s.article.pk)
        context['aricles_like'] = articles_id
        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context


class ArticleView(DetailView):
    model = Article
    template_name = 'articles/view.html'


class CreateArticleView(PermissionRequiredMixin, CreateView):
    template_name = 'articles/create.html'
    form_class = ArticleForm
    model = Article
    success_url = reverse_lazy('article:list')
    permission_required = 'article.add_article'

    def form_valid(self, form):
        tags = form.cleaned_data.pop('tags')

        article = form.save(commit=False)
        article.author = self.request.user
        article.save()

        article.tags.set(tags)
        return redirect(self.get_success_url())


class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = ArticleForm
    model = Article
    template_name = 'articles/update.html'
    context_object_name = 'article'
    permission_required = 'article.change_article'

    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()

    def get_success_url(self):
        return reverse('article:view', kwargs={'pk': self.kwargs.get('pk')})


class ArticleDeleteView(PermissionRequiredMixin, DeleteView):
    model = Article
    template_name = 'articles/delete.html'
    context_object_name = 'article'
    success_url = reverse_lazy('article:list')
    permission_required = 'article.delete_article'


class LikeArticle(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        like = article.like_articles.filter(user=request.user)
        print(like)
        if like.count() == 0:
            Articles_and_users_intermediate_table.objects.create(user=request.user, article=article)
            return JsonResponse({'count': article.like_articles.count()})
        else:
            return HttpResponseForbidden('Лайк уже поставлен', status=403)


class UnLikeArticle(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        like = article.like_articles.filter(user=request.user)
        print(like)
        if like.count() != 0:
            like.delete()
            return JsonResponse({'count': article.like_articles.count()})
        else:
            return HttpResponseForbidden('Лайк не был поставлен', status=403)
