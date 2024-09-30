from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'original_title', 'overview', 'release_date', 'budget', 'revenue',
            'runtime', 'status', 'vote_average', 'vote_count', 'homepage', 'original_language',
            'languages', 'production_company_id', 'genre_id'
        ]
