from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router_v2 = DefaultRouter()
router_v2.get_api_root_view().cls.__name__ = 'Api V.2'
router_v2.register(r'posts', PostViewSet)
router_v2.register(r'groups', GroupViewSet)
router_v2.register(r'follow', FollowViewSet, basename='following')
router_v2.register(r'posts/(?P<post_id>[^/.]+)/comments', CommentViewSet,
                   basename='comments')

urlpatterns = [
    path('v1/', include(router_v2.urls)),
    path(r'v1/', include('djoser.urls')),
    path(r'v1/', include('djoser.urls.jwt')),
]
