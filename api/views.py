from django.shortcuts import render
from rest_framework import viewsets
from .models import Meal, Rating
from .serializers import Mealserializer, Ratingserializer


class Mealviewset(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = Mealserializer


class Ratingviewset(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = Ratingserializer
