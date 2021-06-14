from django.contrib import admin
from .models import Movie,Rating
# Register your models here.

@admin.register(Movie)
class AdminforMovie(admin.ModelAdmin):
    list_display = ['id','title','description']

@admin.register(Rating)
class AdminforRating(admin.ModelAdmin):
    list_display = ['id','movie','stars']