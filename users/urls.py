from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import MyTokenObtainPairView, UserViewSet, PaymentCreateAPIView, PaymentListAPIView, PaymentRetrieveAPIView, PaymentUpdateAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payment/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_get'),
    path('payment/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment_update'),
    
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
] + router.urls
