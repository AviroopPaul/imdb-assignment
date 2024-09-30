from django.urls import path
from imdb_app.views import upload_csv, MovieListView

urlpatterns = [
    path('upload_csv/', upload_csv, name='upload_csv'),
    path('movies/', MovieListView.as_view(), name='movie_list'),
]
