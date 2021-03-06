# For user
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View

# For API
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import AlbumSerializer, SongSerializer

from . models import Album, Song
from . forms import UserForm


# For Webapp
class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # display a blank form
    def get(self, request):
        form = self.form_class(None)
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    # process form
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            # hasn't been saved to db yet
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # Return User objects if credentials correct
            user = authenticate(username=username, password=password)

            if user:

                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})


# For API
class AlbumList(APIView):

    def get(self, request):
        albums = Album.objects.all()
        album_serializer = AlbumSerializer(albums, many=True)
        return Response(album_serializer.data)

    def post(self):
        pass


class SongList(APIView):

    def get(self, request):
        songs = Song.objects.all()
        song_serializer = SongSerializer(songs, many=True)
        return Response(song_serializer.data)













#
