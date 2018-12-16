from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.posts, name='posts'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
    url(r'^user_details/(?P<id>\d+)/$', views.user_details, name='user_details')
]