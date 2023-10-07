from rest_framework import serializers
from .models import Meal, Rating


class Mealserializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"


class Ratingserializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"

