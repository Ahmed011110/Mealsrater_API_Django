from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db.models import Model


# uuid
class Meal(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=400)
    price = models.IntegerField()
    fields = "__all__"

    def __str__(self):
        return self.title


class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    # stars = models.CharField(max_length=50)  len=(20), validators=[MinLengthValidator(1), MaxLengthValidator(5)]
    fields = "__all__"

    # def __str__(self):
    #     return self.meal

    class Meta:
        unique_together = (("user", "meal"),)
        index_together = (("user", "meal"),)
