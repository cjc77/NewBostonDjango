from django.conf.urls import url
from . import views

# For API
from rest_framework.urlpatterns import format_suffix_patterns
from music import views

app_name = "music"

urlpatterns = [
    # 'name' represents the associated url pattern
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /music/pk/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/pk/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/pk/delete/
    url(r'album/(?P<pk>[0-9]+)/delete$', views.AlbumDelete.as_view(), name='album-delete'),


    # API
    # music/albums
    url(r'^albums', views.AlbumList.as_view(), name="album-list-JSON"),

    # music/songs
    url(r'^songs', views.SongList.as_view(), name="song-list-JSON")
]

# For API
urlpatterns = format_suffix_patterns(urlpatterns)
