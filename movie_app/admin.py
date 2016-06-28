from django.contrib import admin

from movie_app.models import Movie, Rating, Rater

# Register your models here.
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Rater)
