from django.contrib import admin

from news_app.models import Post, Tag, User

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Tag)
