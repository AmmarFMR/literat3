from django.urls import path
from .views import PostsListView, PostsDetailView

urlpatterns = [
    path('', PostsListView.as_view()),
    path('<pk>', PostsDetailView.as_view())
]