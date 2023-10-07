from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import Mealviewset, Ratingviewset


router = routers.DefaultRouter()
router.register("meal", Mealviewset)
router.register("rating", Ratingviewset)


urlpatterns = [
    path("", include(router.urls)),
]
