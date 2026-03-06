from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Movie


def index(request):
    latest_movie_list = Movie.objects.order_by("-release_date")[:5]
    template = loader.get_template("bookings/index.html")
    context = {"latest_movie_list": latest_movie_list}
    return HttpResponse(template.render(context, request))


def detail(request, movie_id):
    return HttpResponse("You're looking at movie %s.", movie_id)
