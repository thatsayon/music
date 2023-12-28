from django.shortcuts import render, redirect
from . import forms
from . import models

def musician(request):
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('Home')
    else:
        musician_form = forms.MusicianForm()
    return render(request, 'musician.html', {'form':musician_form})

def editmusician(request, id):
    musician = models.MusicModel.objects.get(pk=id)
    musician_form = forms.MusicianForm(instance=musician)
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('Home')
    return render(request, 'musician.html', {'form': musician_form})

def album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('Home')
    else:
        album_form = forms.AlbumForm()
    return render(request, 'album.html', {'form': album_form})

def editalbum(request, id):
    album = models.AlbumModel.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=album)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('Home')
    return render(request, 'musician.html', {'form': album_form})

def deletealbum(request, id):
    album = models.AlbumModel.objects.get(pk=id)
    album.delete()
    return redirect("Home")