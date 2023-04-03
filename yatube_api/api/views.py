from django.shortcuts import get_object_or_404
from rest_framework import viewsets, pagination
from rest_framework.filters import SearchFilter

from posts.models import Post, Group, Comment, Follow
from .permissions import IsAuthorOrReadOnly, IsAuthenticated
from .serializers import (PostSerializer, GroupSerializer,
                          CommentSerializer, FollowSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author', 'group')
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related('post')
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_post(self):
        return get_object_or_404(
            Post, pk=self.kwargs.get('post_id')
        )

    def get_queryset(self):
        return self.get_post().comments

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.select_related('user')
    serializer_class = FollowSerializer
    pagination_class = pagination.LimitOffsetPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('following__username', 'user__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
