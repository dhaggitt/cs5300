from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    release_date = models.DateField()
    movie_duration = DurationField()