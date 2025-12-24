from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'tmdb_id', 'title', 'original_title', 'digital_release_date', 'poster_path', 'overview', 'genres']
