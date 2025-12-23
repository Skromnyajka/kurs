from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    STATUS_CHOICES = [
        ('new', 'На согласовании'),
        ('approved', 'Согласовано'),
        ('rejected', 'Отклонено'),
    ]

    title = models.CharField('Тема документа', max_length=200)
    # Обновили название поля для понятности
    content = models.TextField('Содержание / Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='new')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    # Обновили параметры загрузки файла
    file = models.FileField('Файл (скан/оригинал)', upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'