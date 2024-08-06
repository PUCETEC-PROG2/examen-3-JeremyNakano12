from django import forms
from .models import Artist, Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'release_year': forms.DateInput(attrs={
                'class':'form-control',
                'type': 'date'
            }),
            'genre': forms.Select(attrs={
                'class':'form-control'
            }),
            'artist': forms.Select(attrs={
                'class':'form-control'
            }),
            'cover': forms.ClearableFileInput(attrs={
            })
        }
        
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        widgets = {
            'artist_name': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'country': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'picture': forms.ClearableFileInput(attrs={
            })
        }