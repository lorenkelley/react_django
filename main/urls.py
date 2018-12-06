from django.urls import path, include
from rest_framework import routers

from main import views

router = routers.DefaultRouter()
router.register('artists', views.ArtistView)
router.register('songs', views.SongView)

urlpatterns = [
    path('', include(router.urls))
]