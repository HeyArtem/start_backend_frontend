from blog_app.models import BlogPost, BlogPostCategory, BlogPostTag
from blog_app.api.serializer import BlogPostListSerializer
from rest_framework import generics


class BlogPostListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.filter(status='published')
    serializer_class = BlogPostListSerializer
