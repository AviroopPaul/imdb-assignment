"""
URL configuration for imdb_assignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from imdb_app import views
from imdb_app import urls as imdb_app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_page, name='upload'),
    path('movies/', views.movie_list_page, name='movie_list'),
    path('api/', include(imdb_app_urls)),
    path('', RedirectView.as_view(url='/upload/', permanent=True)),  # Redirect root URL to /upload/
]
