from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    release_date = models.DateField()
    movie_duration = models.DurationField()

class Seat(models.Model):
    seat_number = models.IntegerField()
    booking_status = models.CharField(max_length=20)

class Booking(models.Model):
    movie = models.ForeignKey(Movie)
    seat = models.ForeignKey(Seat)
    user = models.CharField(max_length=100)
    booking_date = models.DateField()