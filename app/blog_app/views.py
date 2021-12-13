from django.shortcuts import render
from .models import BlogPost
from blog_app.api.serializer import (
    BlogPostListSerializer,
    BlogPostDetailSerializer,
    BlogPostSerializer,    
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

# реализация сериалайзера через ФУНКЦИЮ (активация в urls)
@api_view(['GET', 'POST'])

# метод GET возвращает (показывает) посты
def blog_post_list(request):    
    if request.method == 'GET':
        blod_posts = BlogPost.objects.filter(status='published')
        # blod_posts = BlogPost.objects.all()
        serializer = BlogPostListSerializer(blod_posts, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # меод 'POST' создает пост
    elif request.method == 'POST':
        serializer = BlogPostListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # если не POST и не GET возвращается ошибка
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# модель через КЛАСС (гибрид класса и функции), промежуточная модель между функциями и дженериками
class BlogPostListCreateAPIView(APIView):
    def get(self, request):
        blod_posts = BlogPost.objects.all()
        serializer = BlogPostListSerializer(blod_posts, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BlogPostListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # если не POST и не GET возвращается ошибка
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
    
    
# реализация сериалайзера через ДЖЕНЕРИКИ (активация в urls)
class BlogPostListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.filter(status='published')
    serializer_class = BlogPostListSerializer
    
    
class BlogPostDetailAPIView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.filter(status='published')
    serializer_class = BlogPostDetailSerializer
    
    
class BlogPostCreateAPIView(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
