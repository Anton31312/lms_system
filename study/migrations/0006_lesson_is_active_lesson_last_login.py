# Generated by Django 5.0.6 on 2024-06-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0005_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата успешного входа'),
        ),
    ]