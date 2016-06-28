from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics  # listAPI basic view

import json  # built in python library. we use to convert dict to str (.dumps, .loads)
from movie_app.models import Movie, Rater, Rating
from movie_app.serializers import MovieSerializer, RaterSerializer


class MovieListAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class RaterListAPIView(generics.ListCreateAPIView):
    queryset = Rater.objects.all()
    serializer_class = RaterSerializer

class RaterDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rater.objects.all()
    serializer_class = RaterSerializer
