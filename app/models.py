from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db.models.fields import TextField
from django.utils import timezone
# Create your models here.


class Categories(models.Model):
    title = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.title


class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=18)
    description = models.CharField(max_length=200)
    image_URl = models.ImageField(upload_to="images/")
    publised_on = models.DateTimeField(editable=False)
    price = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0, null=True)
    avg_ratings = models.IntegerField(
        default=5, validators=[MinLengthValidator(1), MaxValueValidator(5)], null=True)
    rating_count = models.PositiveIntegerField(default=0, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.publised_on = timezone.now()
        return super(Products, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class Reviews(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MaxValueValidator(1), MaxValueValidator(5)])
    body = TextField(max_length=4000, null=True)
    created_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super(Reviews, self).save(*args, **kwargs)
