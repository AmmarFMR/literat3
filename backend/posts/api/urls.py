from posts.api.views import PostsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PostsViewSet, base_name='posts')
urlpatterns = router.urls

# from django.urls import path
# from .views import PostsListView, PostsDetailView, PostsCreateView, PostsDeleteView, PostsUpdateView

# urlpatterns = [
#     path('', PostsListView.as_view()),
#     path('create/', PostsCreateView.as_view()),
#     path('<pk>/update/', PostsUpdateView.as_view()),
#     path('<pk>/delete/', PostsDeleteView.as_view()),
#     path('<pk>', PostsDetailView.as_view())
# ]