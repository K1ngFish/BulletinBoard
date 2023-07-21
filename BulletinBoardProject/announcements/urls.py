from django.urls import path

from .views import AnnouncementsList, AnnouncementDetail, \
    AnnouncementCreate, AnnouncementUpdate, AnnouncementDelete, SearchResultsView, CreateResponseView, \
    accept_response, reject_response, delete_response, PrivatePageView

urlpatterns = [
    path('', AnnouncementsList.as_view(), name = 'announcement_list'),
    path('<int:pk>', AnnouncementDetail.as_view(), name = 'announcement_detail'),
    path('my_responses/', PrivatePageView.as_view(), name='private_page'),
    path('create/', AnnouncementCreate.as_view(), name = 'announcement_create'),
    path('<int:pk>/update/', AnnouncementUpdate.as_view(), name = 'announcement_update'),
    path('<int:pk>/delete/', AnnouncementDelete.as_view(), name = 'announcement_delete'),
    path('search/', SearchResultsView.as_view(), name='post_search'),
    path('announcement/<int:pk>/create_response/', CreateResponseView.as_view(), name='create_response'),
    path('response/accept/<int:response_id>/', accept_response, name='accept_response'),
    path('response/reject/<int:response_id>/', reject_response, name='reject_response'),
    path('response/delete/<int:response_id>/', delete_response, name='delete_response'),
]