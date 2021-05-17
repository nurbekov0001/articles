from django.contrib import admin
from article.models import Article, Tag, Comment, Articles_and_users_intermediate_table
from article.models import Intermediate_table_of_cometaries_and_users

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at', 'updated_at']
    list_filter = ['author', 'tags']
    search_fields = ['title', 'content', 'tags']
    fields = ['id', 'title', 'author', 'tags', 'content', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at', 'id', 'author']


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', 'created_at', 'updated_at']
    list_filter = ['tag']
    search_fields = ['tag']
    fields = ['id', 'tag', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'comment', 'author', 'created_at', 'updated_at']
    list_filter = ['article', 'author']
    search_fields = ['article', 'comment', 'author']
    fields = ['id', 'article', 'comment', 'author', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'author', 'updated_at']

class LikesAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'user']

class LikesCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'user']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Articles_and_users_intermediate_table, LikesAdmin)
admin.site.register(Intermediate_table_of_cometaries_and_users, LikesCommentAdmin)
