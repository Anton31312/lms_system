from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from study.models import Course, Lesson

NULLABLE = {'blank': True, 'null':True}

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='автар', **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='город', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Payment(models.Model):

    PAYMENT_METHOD = [
        ('cash', 'наличные'),
        ('card', 'перевод на счёт'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    date = models.DateField(verbose_name='дата оплаты', default=timezone.now)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="курс", **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="урок", **NULLABLE)
    payment_amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_met = models.CharField(max_length=50, choices=PAYMENT_METHOD, verbose_name='способ оплаты',
                              default='cash')

    def __str__(self) -> str:
        return f'{self.user}: {self.course if self.course else self.lesson} - {self.payment_amount} руб.'
    
    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежей'
        ordering = ('date',)
