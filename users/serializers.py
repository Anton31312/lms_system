from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import Payment, User

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    payment_history = PaymentSerializer(source='payment_set', many=True)

    class Meta:
        model = User
        fields = '__all__'

 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['email'] = user.email
        token['password'] = user.password

        return token


       