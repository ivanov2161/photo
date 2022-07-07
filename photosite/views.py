from django.shortcuts import render
from .models import Photos, Album
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def home(request):
    photos = Photos.objects.all()
    return render(request, 'home.html', {'photos': photos[4]})


def about(request):
    return render(request, 'about.html')


def albums(request):
    temp = dict()
    albums = Album.objects.all()
    photos = Photos.objects.all()
    for i in photos:
        temp[str(i.album)] = i.photo.url
    return render(request, 'albums.html', {'albums': albums, 'temp': temp})


def show_album(request, album):
    photos = Photos.objects.filter(album=album)
    albums = Album.objects.get(pk=album)
    return render(request, 'show_album.html', {'photos': photos, 'album': albums})
