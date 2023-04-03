from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from .views import (PostViewSet, GroupViewSet, 
                    CommentViewSet, FollowViewSet)

app_name = 'api'

router = routers.DefaultRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='commentviewset')
router.register('follow', FollowViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
