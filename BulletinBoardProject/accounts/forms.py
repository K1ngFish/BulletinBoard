import random

from allauth.account.forms import SignupForm
from django.core.mail import send_mail
from django.conf import settings
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        confirmation_code = ''.join(random.choices('0123456789', k=4))
        user.profile.confirmation_code = confirmation_code
        user.profile.save()
        subject = 'Confirmation Code for Your Account'
        message = f'Hello, your confirmation code is: {confirmation_code}. ' \
                  f'Please enter it at this link: http://127.0.0.1:8000/accounts/confirm_registration/'
        from_email = settings.EMAIL_HOST_USER
        to_email = user.email
        send_mail(subject, message, from_email, [to_email])
        return user
