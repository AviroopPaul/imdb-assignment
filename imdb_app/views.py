import pandas as pd
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import transaction
from .models import Movie
from .serializers import MovieSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter  # Added SearchFilter
import numpy as np
from datetime import datetime
from rest_framework.pagination import PageNumberPagination  # Newly added import

@api_view(['POST'])
def upload_csv(request):
    file = request.FILES.get('file')
    if not file:
        return Response({"error": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)
        
    if not file.name.endswith('.csv'):
        return Response({"error": "Only CSV files are allowed."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        df = pd.read_csv(file)
    except Exception as e:
        return Response({"error": f"Error reading CSV file: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    # Define the expected columns and their types
    expected_columns = {
        'title': 'string',
        'original_title': 'string',
        'overview': 'string',
        'release_date': 'datetime',
        'budget': 'float',
        'revenue': 'float',
        'runtime': 'float',
        'status': 'string',
        'vote_average': 'float',
        'vote_count': 'float',
        'homepage': 'string',
        'original_language': 'string',
        'languages': 'string',
        'production_company_id': 'float',
        'genre_id': 'float',
    }

    # Ensure all expected columns are present
    missing_columns = set(expected_columns.keys()) - set(df.columns)
    if missing_columns:
        return Response({"error": f"Missing columns: {', '.join(missing_columns)}"}, status=status.HTTP_400_BAD_REQUEST)

    # Fill missing values based on type
    for column, dtype in expected_columns.items():
        if dtype == 'string':
            df[column] = df[column].fillna('')
        elif dtype == 'float':
            df[column] = pd.to_numeric(df[column], errors='coerce').fillna(0.0)
        elif dtype == 'datetime':
            df[column] = pd.to_datetime(df[column], errors='coerce')

    movies_to_create = []
    for index, row in df.iterrows():
        # Validate release_date
        release_date = row['release_date'].date() if not pd.isnull(row['release_date']) else None

        movie = Movie(
            title=row['title'],
            original_title=row['original_title'],
            overview=row['overview'],
            release_date=release_date,
            budget=row['budget'],
            revenue=row['revenue'],
            runtime=row['runtime'],
            status=row['status'],
            vote_average=row['vote_average'],
            vote_count=row['vote_count'],
            homepage=row['homepage'] if row['homepage'] else None,
            original_language=row['original_language'],
            languages=row['languages'],
            production_company_id=int(row['production_company_id']) if row['production_company_id'] else None,
            genre_id=int(row['genre_id']) if row['genre_id'] else None,
        )
        movies_to_create.append(movie)
    
    try:
        with transaction.atomic():
            Movie.objects.bulk_create(movies_to_create)
    except Exception as e:
        return Response({"error": f"Database error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({"message": "CSV uploaded and processed successfully"}, status=201)

class MoviePagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'num_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data
        })

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]  # Added SearchFilter
    filterset_fields = ['release_date', 'original_language']
    ordering_fields = ['release_date', 'vote_average', 'budget', 'revenue', 'ratings']
    search_fields = ['title', 'original_title']  # Specify fields to search
    pagination_class = MoviePagination  # Updated to use custom pagination

from django.shortcuts import render

def upload_page(request):
    return render(request, 'imdb_app/upload.html')

def movie_list_page(request):
    return render(request, 'imdb_app/movie_list.html')