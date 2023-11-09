from django.db import models

NULLABLE = {'blank': True, 'null': True}


class BlogPost(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='product_image/', verbose_name='превью', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    publication_sign = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    slug = models.CharField(max_length=100, verbose_name='slug', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'