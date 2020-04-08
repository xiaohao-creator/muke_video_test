from django.urls import path

from .views.auth import Login, AdminManager, Logout, UpdateAdminStatus
from .views.base import Index
from .views.video import ExternalVideo, VideoSubView, VideoStarView, StarDelete

urlpatterns = [
    path('', Index.as_view(), name='dashboard_index'),
    path('login/', Login.as_view(), name='dashboard_login'),
    path('logout', Logout.as_view(), name='dashboard_logout'),
    path('admin/manager', AdminManager.as_view(), name='admin_manager'),
    path('admin/manager/update/status', UpdateAdminStatus.as_view(), name='admin_update_status'),
    path('video/external', ExternalVideo.as_view(), name='external_video'),
    path('video/videosub/<int:video_id>', VideoSubView.as_view(), name='video_sub'),
    path('video/star', VideoStarView.as_view(), name='video_star'),
    path('video/star/delete/<int:star_id>/<int:video_id>',StarDelete.as_view(),name='star_delete')
]
