from django.contrib import admin

# Register your models here.
from blog.models import Author, Cover, Post, Tag

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Cover)
