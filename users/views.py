from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()  

    filter_backends = [DjangoFilterBackend, OrderingFilter]  
    filterset_fields = ('course', 'lesson', 'payment_met',)
    ordering_fields = ('date',)

class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()  

class PaymentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()      

