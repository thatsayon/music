from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class MusicModel(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_num = models.CharField(max_length=14)
    instrument_type = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name


class AlbumModel(models.Model):
    album_name = models.CharField(max_length=30)
    musician = models.ForeignKey(MusicModel, on_delete=models.CASCADE)
    album_release = models.DateField(default=datetime.date.today)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.album_name