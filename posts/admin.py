from django.contrib import admin
from .models import Post, Comment, Category, Upvote, Downvote

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Downvote)
admin.site.register(Upvote)