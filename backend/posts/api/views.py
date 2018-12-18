from rest_framework import viewsets

from posts.models import Posts
from .serializers import PostsSerializer


class PostsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()


# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

# class PostsListView(ListAPIView):
#     queryset = Posts.objects.all()
#     serializer_class = PostsSerializer


# class PostsDetailView(RetrieveAPIView):
#     queryset = Posts.objects.all()
#     serializer_class = PostsSerializer


# class PostsCreateView(CreateAPIView):
#     queryset = Posts.objects.all()
#     serializer_class = PostsSerializer


# class PostsDeleteView(DestroyAPIView):
#     queryset = Posts.objects.all()
#     serializer_class = PostsSerializer


# class PostsUpdateView(UpdateAPIView):
#     queryset = Posts.objects.all()
#     serializer_class = PostsSerializer
