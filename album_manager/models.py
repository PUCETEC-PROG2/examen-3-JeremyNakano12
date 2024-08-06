from django.db import models

# Create your models here.
class Artist (models.Model):
    artist_name = models.CharField(max_length=30, null=False)
    country = models.CharField(max_length=20, null=False)
    picture = models.ImageField(upload_to='artist_picture')

    def __str__(self) -> str:
        return f'{self.artist_name}'

class Album (models.Model):
    title = models.CharField(max_length=50, null=False)
    release_year = models.DateField(null=False)
    MUSIC_GENRE = {
        ('M', 'Metal'),
        ('RK', 'Rock'),
        ('P', 'Pop'),
        ('E', 'Electronic'),
        ('H', 'Hip Hop'),
        ('R', 'Rap'),
        ('I', 'Indie'),
        ('C', 'Classic'),
        ('J', 'Jazz')
    }
    genre = models.CharField(max_length=15, choices=MUSIC_GENRE, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='album_covers')
    def __str__(self) -> str:
        return f'{self.title}'