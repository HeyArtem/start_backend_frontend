from django.db import models


class BlogPostTag(models.Model):
    title = models.CharField(verbose_name='Тэг', max_length=20)
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        
    def __str__(self) -> str:
        return self.title


class BlogPostCategory(models.Model):
    title = models.CharField(verbose_name='Категория', max_length=20)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    def __str__(self) -> str:
        return self.title


class BlogPost(models.Model):
    STATUS_CHOISES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано')
    )
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    category = models.ForeignKey(BlogPostCategory, on_delete=models.SET_NULL, null=True)
    img = models.ImageField(verbose_name='Фото новости', upload_to='blog_app/%Y/%m/%d')
    description = models.CharField(verbose_name='Краткое описание', max_length=100)
    content = models.TextField(verbose_name='Текст')
    creared_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    tag = models.ManyToManyField(BlogPostTag, verbose_name='Тэг', blank=True) 
    status = models.CharField(verbose_name='Статус', choices=STATUS_CHOISES, default='draft', max_length=20)
    
    # класс для кастомизации админки
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        
    # магический метод для вывода имена моделей
    def __str__(self):
        return self.title
