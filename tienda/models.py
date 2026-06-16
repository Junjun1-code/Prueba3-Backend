from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    itemname = models.Charfield(max_length=100)
    price = models.IntegerField(max_length=10)
    stock = models.IntegerField(min = 0)
    img = models.CharField(max_length=100)
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'Users'
    )
    published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo

class Rating(models.model):
    rateditem = models.ForeignKey(
        Item,
        on_delete = models.CASCADE,
        related_name = 'Items'
    )
    stars = models.IntegerField(min = 0, max= 5)
    comments = models.TextField(max_length=150)
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'Users'
    )

    def __str__(self):
        return self.titulo

# Create your models here.
