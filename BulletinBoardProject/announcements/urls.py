from django.urls import path
from .views import AnnouncementsList, AnnouncementDetail, AnnouncementCreate

urlpatterns = [
    path('', AnnouncementsList.as_view()),
    path('<int:pk>', AnnouncementDetail.as_view(), name = 'announcement_detail'),
    path('create/', AnnouncementCreate.as_view(), name = 'announcement_create'),
]