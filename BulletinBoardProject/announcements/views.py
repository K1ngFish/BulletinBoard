from datetime import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .filters import AnnouncementFilter

from .models import Announcement, Response
from .forms import AnnouncementForm


class AnnouncementsList(ListView):
    model = Announcement
    template_name = 'announcements.html'
    context_object_name = 'announcements'
    paginate_by = 2

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

class AnnouncementCreate(CreateView):
    form_class = AnnouncementForm
    model = Announcement
    template_name = 'announcement_edit.html'