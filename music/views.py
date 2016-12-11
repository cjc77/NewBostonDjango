from django.http import Http404
from django.shortcuts import render, get_object_or_404
from . models import Album, Song


def index(request):
    all_albums = Album.objects.all()
    context = {
        "all_albums": all_albums,
    }
    return render(request, "music/index.html", context)


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    context = {
        "album": album,
    }
    return render(request, "music/detail.html", context)


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            "album": album,
            "error_message": "You did not select a valid song.",
        })
    else:
        # Favorite or unfavorite song
        if not selected_song.is_favorite:
            selected_song.is_favorite = True
            selected_song.save()
        elif selected_song.is_favorite:
            selected_song.is_favorite = False
            selected_song.save()
        return render(request, 'music/detail.html', {"album": album})
