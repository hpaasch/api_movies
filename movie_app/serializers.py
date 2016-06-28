from rest_framework import serializers
from movie_app.models import Movie, Rater, Rating

class MovieSerializer(serializers.ModelSerializer):

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


class RatingSerializer(serializers.HyperlinkedModelSerializer):
    movie_title = serializers.SerializerMethodField()

    class Meta:
        model = Rating
        fields = ('user_id', 'item_id', 'rating', 'timestamp', 'movie_title')

    def get_movie_title(self, rating):
        return rating.item_id.movie_title
