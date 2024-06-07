# Generated by Django 5.0.6 on 2024-06-07 12:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0004_delete_subscribe'),
        ('users', '0003_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('subscribe', 'подписан'), ('not_subscribe', 'не подписан')], default='not_subscribe', max_length=50, verbose_name='статус подписки')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.course', verbose_name='курс')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'подписка',
                'verbose_name_plural': 'подписки',
            },
        ),
    ]