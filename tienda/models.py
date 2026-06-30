from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg

class Item(models.Model):
    itemname = models.CharField(max_length=100)
    price = models.IntegerField(validators=[MaxValueValidator(10000000)])
    stock = models.IntegerField(
        validators=[
            MinValueValidator(0)
    ])
    img = models.ImageField(max_length=100)
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'itemuser'
    )
    published = models.BooleanField(default=False)
    
    @property
    def average_rating(self):
        return self.ratings.aggregate(avg=Avg("stars"))["avg"] or 0
    
    def __str__(self):
        return self.itemname
    
    

class Rating(models.Model):
    rateditem = models.ForeignKey(
        Item,
        on_delete = models.CASCADE,
        related_name = 'Items'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ])
    comments = models.TextField(max_length=150)
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'ratinguser'
    )

    def __str__(self):
        return self.rateditem

# Create your models here.
