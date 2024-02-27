from django.db import models


# Create your models here.


class Car(models.Model):
    car_name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.CharField(max_length=255)

    class Meta:
        ordering = ['car_name']


class Owner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    car = models.OneToOneField(
        Car,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    class Meta:
        ordering = ['first_name']
