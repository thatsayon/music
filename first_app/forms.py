from django import forms
from . import models

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.MusicModel
        fields = '__all__'

class AlbumForm(forms.ModelForm):
    class Meta:
        model = models.AlbumModel
        fields = '__all__'