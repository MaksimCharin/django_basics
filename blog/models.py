from django.db import models

class BlogMessage(models.Model):
    title = models.CharField(max_length=50, verbose_name='заголовок')
    description = models.TextField(null=True, blank=True, verbose_name='содержимое')
    preview = models.ImageField(upload_to='photos/', null=True, blank=True, verbose_name='превью(изображение)')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    view_counter = models.PositiveIntegerField(verbose_name='счетчик просмотров', default=0)
