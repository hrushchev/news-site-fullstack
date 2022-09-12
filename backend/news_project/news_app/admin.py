from django.contrib import admin

from news_app.models import User, Post, Tag

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Tag)
