from django.urls import path
from blog_app.api.views import BlogPostListAPIView
    

urlpatterns = [
    # через дженерики
    path('', BlogPostListAPIView.as_view())
    
    # # активация через функцию
    # path('', blog_post_list),
    
    # # активация через гибрид 
    # path('class1/', BlogPostListCreateAPIView.as_view()),
    
    # # через дженерики
    # path('class2/', BlogPostListAPIView.as_view()),
    
    # # детальный вывод при помощи дженериков
    # path('detail/<int:pk>/', BlogPostDetailAPIView.as_view()),
    
    # # через дженерики создание
    # path('create/', BlogPostCreateAPIView.as_view())
]
