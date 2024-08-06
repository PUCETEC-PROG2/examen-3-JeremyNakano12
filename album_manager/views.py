from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from album_manager.forms import AlbumForm, ArtistForm
from .models import Album, Artist

def index(request):
    template = loader.get_template('index.html')
    return render(request, 'index.html')

def album(request, album_id):
    album = get_object_or_404(Album, pk = album_id)
    template = loader.get_template('display_album.html')
    context = {
        'album': album
    }
    return HttpResponse(template.render(context, request))

def artist(request, artist_id):
    artist = get_object_or_404(Artist, pk = artist_id)
    template = loader.get_template('display_artist.html')
    context = {
        'artist': artist
    }
    return HttpResponse(template.render(context, request))

def list_album(request):
    albums = Album.objects.order_by('genre')
    template = loader.get_template('list_album.html')
    return HttpResponse(template.render({'albums': albums}, request))

def list_artist(request):
    artists = Artist.objects.order_by('artist_name')
    template = loader.get_template('list_artist.html')
    return HttpResponse(template.render({'artists': artists}, request))

def add_album(request):
    if request.method =='POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:list_album')
    else:
        form = AlbumForm()
    return render(request, 'album_form.html', {'form':form})

def add_artist(request):
    if request.method =='POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:list_artist')
    else:
        form = ArtistForm()
    return render(request, 'artist_form.html', {'form':form})

def edit_album(request, album_id):
    album = get_object_or_404(Album, pk = album_id) 
    if request.method =='POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_manager:list_album')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album_form.html', {'form':form})

def edit_artist(request, artist_id):
    artist = get_object_or_404(Artist, pk = artist_id) 
    if request.method =='POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('album_manager:list_artist')
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'artist_form.html', {'form':form})

def delete_album(request, album_id):
    album = get_object_or_404(Album, pk = album_id)
    album.delete()
    return redirect("album_manager:list_album")

def delete_artist(request, artist_id):
    artist = get_object_or_404(Artist, pk = artist_id)
    artist.delete()
    return redirect("album_manager:list_artist")
