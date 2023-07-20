from django.urls import path
from .views import SignUp, confirm_registration, ConfirmEmailView

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('confirm-email/<str:key>/', ConfirmEmailView.as_view(), name='account_confirm_email'),
    path('confirm_registration/', confirm_registration, name='confirm_registration'),
]
