from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from . models import Album


def index(request):
    all_albums = Album.objects.all()
    context = {
        "all_albums": all_albums,
    }
    return render(request, "music/index.html", context)


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("This Album does not currently exist.")
    context = {
        "album": album,
    }
    return render(request, "music/detail.html", context)
