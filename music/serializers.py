from rest_framework import serializers
from . models import Album, Song


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        # fields = ('artist', 'album_title', 'genre', 'album_logo')
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        # fields = ('album', 'file_type', 'song_title', 'is_favorite')
        fields = '__all__'
