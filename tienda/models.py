from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Item(models.Model):
    itemname = models.CharField(max_length=100)
    price = models.IntegerField(max_length=10)
    stock = models.IntegerField(
        validators=[
            MinValueValidator(0)
    ])
    img = models.CharField(max_length=100)
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'Users'
    )
    published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
    
    

class Rating(models.Model):
    rateditem = models.ForeignKey(
        Item,
        on_delete = models.CASCADE,
        related_name = 'Items'
    )

    # STARS_CHOICES = [(i, str(i)) for i in range(1,6)]
    # stars = models.PositiveSmallIntegerField(
    #     choices=STARS_CHOICES
    # )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ])
    comments = models.TextField(max_length=150)
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'Users'
    )

    def __str__(self):
        return self.titulo

# Create your models here.
