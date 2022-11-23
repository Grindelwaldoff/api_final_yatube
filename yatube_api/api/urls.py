from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from django.urls import include, path

from api.views import PostViewSet, GroupViewSet, CommentsViewSet, FollowViewSet


router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentsViewSet,
    basename='comments'
)
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/jwt/', views.obtain_auth_token),
    path('v1/', include(router.urls))
]
