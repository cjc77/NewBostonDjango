from django.conf.urls import url
from . import views

app_name = "music"

urlpatterns = [
    # 'name' represents the associated url pattern
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),


]
