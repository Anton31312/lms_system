# Generated by Django 5.0.6 on 2024-06-11 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0006_lesson_is_active_lesson_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='last_login',
        ),
    ]
