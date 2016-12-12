from django.conf.urls import url
from . import views

app_name = "music"

urlpatterns = [
    # 'name' represents the associated url pattern
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /music/pk/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

]
