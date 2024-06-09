from django.core.management import BaseCommand

from study.models import Lesson
from users.models import Payment, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        payment = Payment.objects.create(
            user=User.objects.get(pk=1),
            lesson=Lesson.objects.get(pk=1),
            payment_amount=1000
        )
        payment.save()