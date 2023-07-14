from django.urls import path
from .views import AnnouncementsList, AnnouncementDetail

urlpatterns = [
    path('', AnnouncementsList.as_view()),
    path('<int:pk>', AnnouncementDetail.as_view()),
]