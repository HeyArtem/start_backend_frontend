from django.db import models
from django.db.models import fields
from blog_app.models import BlogPost, BlogPostCategory, BlogPostTag
from rest_framework import serializers


# сериализатор связанной модели категорий
class BlogPostCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogPostCategory
        fields = '__all__'
        
        
#  сериализатор связанной модели тэгов
class BlogPostTagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogPostTag
        fields = '__all__'


# общий (главный сериализатор) основной модели. Также, для отображения не только id, но и корректного имени поля, в него поместил (расширил) сериализаторы связанных моделей
class BlogPostListSerializer(serializers.ModelSerializer):
    
    # для корректного отбра-я, вложил сюда сериалайзеры 
    category = BlogPostCategorySerializer()
    
    # !!! many=True - тэги это множество!, означает, что тэгов может быть несколько
    tag = BlogPostTagSerializer(many=True)
    
    class Meta:
        model = BlogPost
        # fields = '__all__'
        
        # оставлю для отображения только нужные поля
        fields = ('id', 'title', 'tag', 'category', 'img', 'description', 'updated_at')
        
        # # можно конкретно прописать какие поля сериализовать
        # fields = ('id', 'img', 'description')
        
        # # или сериализовать все кроме
        # exclude = ('content')
        

class BlogPostDetailSerializer(serializers.ModelSerializer):
    # для корректного отбра-я, вложил сюда сериалайзеры 
    category = BlogPostCategorySerializer()
    
    # !!! many=True - тэги это множество!, означает, что тэгов может быть несколько
    tag = BlogPostTagSerializer(many=True)
    
    class Meta:
        model = BlogPost        
        
        # оставлю для отображения только нужные поля
        exclude = ('status', 'creared_at')
        
        
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
