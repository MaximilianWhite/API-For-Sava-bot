# Generated by Django 4.1.4 on 2022-12-16 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsersBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя пользователя')),
                ('age', models.IntegerField(max_length=10, verbose_name='Возраст пользователя')),
                ('city', models.CharField(max_length=150, verbose_name='Город пользователя')),
                ('id_vk', models.CharField(max_length=255, verbose_name='ID VK пользователя')),
                ('instagram_id', models.CharField(max_length=255, verbose_name='Instagram пользователя')),
            ],
        ),
    ]
