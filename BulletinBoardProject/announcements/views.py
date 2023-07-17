from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import AnnouncementFilter
from .models import Announcement, Response
from .forms import AnnouncementForm


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
        return context

class AnnouncementDetail(DetailView):
    model = Announcement
    template_name = 'announcement.html'
    content_object_name = 'announcement'

class AnnouncementCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'announcement_edit.html'

class AnnouncementUpdate(UpdateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'announcement_edit.html'
    success_url = reverse_lazy('announcement_list')

class AnnouncementDelete(DeleteView):
    model = Announcement
    template_name = 'announcement_delete.html'
    success_url = reverse_lazy('announcement_list')