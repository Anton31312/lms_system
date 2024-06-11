from django.core.management import BaseCommand

from study.models import Course
from users.models import Payment, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='test@sky.pro',
            first_name='Test',
            last_name='SkyPro',
            is_staff=True,
            is_active=True
        )
        user.set_password('123qwe456rty')
        user.save()

        course = Course.objects.create(
            title='Изучение Go с нуля'
        )
        course.save()

        payment = Payment.objects.create(
            user=User.objects.get(pk=1),
            course=Course.objects.get(pk=1),
            payment_amount=1000
        )
        payment.save()