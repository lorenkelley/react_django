from rest_framework import serializers

from .models import  Artist, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        field = ('id', 'title', 'preview_url', 'artist', 'album')

class ArtistSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ('id', 'name', 'photo_url', 'nationality', 'songs')