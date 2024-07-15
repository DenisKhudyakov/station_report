from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Класс для пользователя"""
    username = models.CharField(max_length=100, name='Имя пользователя', unique=True)

    REQUIRED_FIELDS = []  # обязательные поля

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username