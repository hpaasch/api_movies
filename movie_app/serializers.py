from rest_framework import serializers

from movie_app.models import Movie, Rater

class MovieSerializer(serializers.ModelSerializer):
    # add data you want to calculate

    class Meta:
        model = Movie
        fields = ('movie_id', 'movie_title', 'release_date',
            'video_release_date', 'imdb_url', 'unknown', 'action',
            'adventure', 'animation', 'children', 'comedy', 'crime',
            'documentary', 'drama', 'fantasy', 'film_noir', 'horror',
            'musical', 'mystery', 'romance', 'scifi', 'thriller',
            'war', 'western')


class RaterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rater
        fields = ('user_id', 'age', 'gender', 'occupation', 'zip_code')
