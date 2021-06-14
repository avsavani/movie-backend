from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50,unique=True)
    description = models.TextField(max_length=500)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        ratings = Rating.objects.filter(movie=self)
        if len(ratings)>0:
            return sum(x.stars for x in  ratings)/len(ratings)
        else:
            return None

    def __str__(self):
        return self.title

class Rating(models.Model):
    stars = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.id