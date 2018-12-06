from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import ArtistSerializer, SongSerializer
from .models import Artist, Song


class ArtistView(viewsets.ModelViewSet):
    # data we get from the database
    queryset = Artist.objects.all()
    # the output of what the data wil look like
    serializer_class = ArtistSerializer

class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer