from django.contrib import admin
from .models import BlogPost, BlogPostTag, BlogPostCategory

admin.site.register(BlogPost)
admin.site.register(BlogPostTag)
admin.site.register(BlogPostCategory)
