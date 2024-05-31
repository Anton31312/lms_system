from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null':True}

class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='study/', verbose_name='превью', **NULLABLE)
    descriprion = models.TextField(verbose_name='описание', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    descriprion = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='study/', verbose_name='превью', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="курс")
    url_link = models.CharField(max_length=500, verbose_name='ссылка на видео')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
    
