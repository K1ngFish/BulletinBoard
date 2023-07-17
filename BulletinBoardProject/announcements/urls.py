from django.urls import path
from .views import AnnouncementsList, AnnouncementDetail, \
    AnnouncementCreate, AnnouncementUpdate, AnnouncementDelete, SearchResultsView

urlpatterns = [
    path('', AnnouncementsList.as_view(), name = 'announcement_list'),
    path('<int:pk>', AnnouncementDetail.as_view(), name = 'announcement_detail'),
    path('create/', AnnouncementCreate.as_view(), name = 'announcement_create'),
    path('<int:pk>/update/', AnnouncementUpdate.as_view(), name = 'announcement_update'),
    path('<int:pk>/delete/', AnnouncementDelete.as_view(), name = 'announcement_delete'),
    path('search/', SearchResultsView.as_view(), name='post_search'),
]