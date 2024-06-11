from datetime import datetime
import pytz
from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from config import settings
from users.models import Payment, User
from users.serializers import MyTokenObtainPairSerializer, PaymentSerializer, UserSerializer
from users.services import create_stripe_price, create_stripe_product, create_stripe_session

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        payment = serializer.save()
        payment.user = self.request.user
        stripe_product_id = create_stripe_product(payment)
        payment.amount = payment.payment_amount
        price = create_stripe_price(stripe_product_id=stripe_product_id, amount=payment.amount)
        session_id, payment_link = create_stripe_session(price=price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()

class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()  
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, OrderingFilter]  
    filterset_fields = ('course', 'lesson', 'payment_met',)
    ordering_fields = ('date',)

class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()  
    permission_classes = [IsAuthenticated]

class PaymentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()  
    permission_classes = [IsAuthenticated]   

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def perform_authentication(self, request):
        user = User.objects.filter(verification_code=self.request.token).first()
        if user:
            zone = pytz.timezone(settings.TIME_ZONE)
            user.last_login = datetime.now(zone)
            user.save()