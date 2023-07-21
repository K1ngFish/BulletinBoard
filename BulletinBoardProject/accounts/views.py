from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from allauth.account.views import ConfirmEmailView

from .forms import CustomSignupForm

class SignUp(CreateView):
    model = User
    form_class = CustomSignupForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'

@login_required
def confirm_registration(request):
    if request.method == 'POST':
        confirmation_code = request.POST.get('confirmation_code', None)
        if confirmation_code and confirmation_code == request.user.profile.confirmation_code:
            request.user.profile.confirmation_code = None
            request.user.profile.save()

            common_users_group = Group.objects.get(name="common users")
            request.user.groups.add(common_users_group)

            request.user.is_active = True
            request.user.save()

            messages.success(request, 'Код подтверждения верный! Аккаунт успешно активирован.')
            return redirect('/announcements')
        else:
            messages.error(request, 'Код подтверждения неверный!')
    return render(request, 'registration/confirm_registration.html')



