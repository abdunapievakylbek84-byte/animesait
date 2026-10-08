from django.db import models

from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=200, verbose_name='Manga'
    )
    author = models.CharField(max_length=100, verbose_name='Автор')
    description = models.TextField(verbose_name='Аннотация')
    content = models.TextField(verbose_name='Текст для чтения')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата добавления'
    )

    def str(self):
        return self.title
    
    
class Book(models.Model):
    title = models.CharField(max_length=255)  # или как у вас называется поле с названием
    # ... остальные поля ...

    def __str__(self):
        return self.title  # Возвращает название книги в админке