from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime

class Movie(models.Model):
    title = models.TextField()
    original_title = models.TextField(blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    release_date = models.DateField(null=True, blank=True)
    budget = models.BigIntegerField(null=True, blank=True)
    revenue = models.BigIntegerField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    status = models.TextField(blank=True, null=True)
    vote_average = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    vote_count = models.IntegerField(null=True, blank=True)
    homepage = models.TextField(null=True, blank=True)
    original_language = models.TextField(blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    production_company_id = models.IntegerField(null=True, blank=True)
    genre_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title