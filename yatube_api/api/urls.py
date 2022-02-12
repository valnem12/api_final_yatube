from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router_v1 = DefaultRouter()
router_v1.get_api_root_view().cls.__name__ = 'Api V.1.2'
router_v1.register(r'posts', PostViewSet)
router_v1.register(r'groups', GroupViewSet)
router_v1.register(r'follow', FollowViewSet, basename='following')
router_v1.register(r'posts/(?P<post_id>[^/.]+)/comments', CommentViewSet,
                   basename='comments')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path(r'v1/', include('djoser.urls')),
    path(r'v1/', include('djoser.urls.jwt')),
]
