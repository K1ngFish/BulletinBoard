from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import EmailMessage
from django.contrib import messages

from .filters import AnnouncementFilter
from .models import Announcement, Response
from .forms import AnnouncementForm, ResponseForm


class AnnouncementsList(ListView):
    model = Announcement
    template_name = 'announcements.html'
    context_object_name = 'announcements'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AnnouncementFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = timezone.now()
        return context

class AnnouncementDetail(DetailView):
    model = Announcement
    template_name = 'announcement.html'
    content_object_name = 'announcement'
    # Функция ниже - новая
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['response_form'] = ResponseForm()
        current_user_responses = Response.objects.filter(
            author=self.request.user,
            announcement=self.object
        )
        context['user_responses'] = current_user_responses
        return context

class AnnouncementCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('announcements.add_announcement',)
    raise_exception = True
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'announcement_edit.html'
    success_url = reverse_lazy('announcement_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AnnouncementUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('announcements.update_announcement',)
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'announcement_edit.html'
    success_url = reverse_lazy('announcement_list')

class AnnouncementDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('announcements.delete_announcement',)
    model = Announcement
    template_name = 'announcement_delete.html'
    success_url = reverse_lazy('announcement_list')

class SearchResultsView(ListView):
    model = Announcement
    template_name = 'search.html'
    context_object_name = 'search_list'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AnnouncementFilter(self.request.GET, queryset)
        queryset = queryset.order_by('-date_creation')
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.now()
        return context

class CreateResponseView(CreateView):
    model = Response
    form_class = ResponseForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.announcement = Announcement.objects.get(pk=self.kwargs['pk'])
        response = super().form_valid(form)
        self.send_email_to_author(form.instance)
        messages.success(self.request, 'Отклик успешно добавлен.')

        current_user_responses = Response.objects.filter(
            author=self.request.user,
            announcement=form.instance.announcement
        )
        for resp in current_user_responses:
            if resp != form.instance:
                resp.accepted = False
                resp.save()
                send_notification_email(resp, accepted=False)

        return response

    def get_success_url(self):
        return reverse('announcement_detail', kwargs={'pk': self.kwargs['pk']})

    def send_email_to_author(self, response):
        subject = f"Отклик на ваше объявление {response.announcement.title}"
        message = (
            f"Пользователь {response.author.username} оставил отклик под вашим объявлением {response.announcement.title}.\n"
            f"Текст отклика: {response.text}"
        )
        from_email = "mailfortestprojects@yandex.ru"
        to_email = response.announcement.author.email
        email = EmailMessage(subject, message, from_email, [to_email])
        email.send()

    def get_success_url(self):
        return reverse('announcement_detail', kwargs={'pk': self.kwargs['pk']})


@login_required
def accept_response(request, response_id):
    response = get_object_or_404(Response, id=response_id)
    if request.user != response.announcement.author:
        return HttpResponseForbidden("Вы не можете принимать отклики на этом объявлении.")
    response.accepted = True
    response.save()
    send_notification_email(response, accepted=True)
    messages.success(request, 'Отклик принят.')
    return redirect('announcement_detail', pk=response.announcement.pk)

@login_required
def reject_response(request, response_id):
    response = get_object_or_404(Response, id=response_id)
    if request.user != response.announcement.author:
        return HttpResponseForbidden("Вы не можете отклонять отклики на этом объявлении.")
    response.accepted = False
    response.save()
    send_notification_email(response, accepted=False)
    messages.success(request, 'Отклик отклонен.')
    return redirect('announcement_detail', pk=response.announcement.pk)

@login_required
def delete_response(request, response_id):
    response = get_object_or_404(Response, id=response_id)
    if request.user == response.author or request.user == response.announcement.author:
        response.delete()
        messages.success(request, 'Отклик удален.')
    else:
        return HttpResponseForbidden("Вы не можете удалять этот отклик.")
    return redirect('announcement_detail', pk=response.announcement.pk)

def send_notification_email(response, accepted=True):
    status_text = "принят" if accepted else "отклонен"
    subject = f"Отклик на ваше объявление {response.announcement.title}"
    message = (
        f"Здравствуйте пользователь {response.author.username}! {response.announcement.author.username}, "
        f"автор объявления {response.announcement.title}, принял решение по отклику. Его статус: {status_text}."
    )
    from_email = "mailfortestprojects@yandex.ru"
    to_email = response.author.email
    email = EmailMessage(subject, message, from_email, [to_email])
    email.send()

class PrivatePageView(ListView):
    model = Announcement
    template_name = 'private_page.html'
    context_object_name = 'private_page'

    def get_queryset(self):
        return Announcement.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        private_page = context['private_page']
        other_users_responses = Response.objects.filter(announcement__in=private_page).exclude(author=self.request.user)
        context['other_users_responses'] = other_users_responses
        return context
