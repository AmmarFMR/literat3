from rest_framework.generics import ListAPIView, RetrieveAPIView
from posts.models import Posts
from .serializers import PostsSerializer

class PostsListView(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class PostsDetailView(RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer