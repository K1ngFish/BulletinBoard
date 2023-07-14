from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput

from .models import Announcement

class AnnouncementFilter(FilterSet):
   dateCreation = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        )
    )

   class Meta:
       model = Announcement
       fields = {
           'title',
           'category',
            }