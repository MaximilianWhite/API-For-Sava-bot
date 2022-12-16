from django.db import models

class UsersBot(models.Model):
    id_files = models.CharField(max_length=150, default='', verbose_name='ID Файла')
    name = models.CharField(max_length=150, default='', verbose_name='Имя пользователя')
    surname = models.CharField(max_length=150, default='', verbose_name='Фамилия пользователя')
    age = models.CharField(max_length=10, default='', verbose_name='Возраст пользователя')
    city = models.CharField(max_length=150, default='', verbose_name='Город пользователя')
    id_vk = models.CharField(max_length=255, default='', verbose_name='ID VK пользователя')
    instagram_id = models.CharField(max_length=255, default='', verbose_name='Instagram пользователя')