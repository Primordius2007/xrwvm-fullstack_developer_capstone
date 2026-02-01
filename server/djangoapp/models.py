from django.db import models

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=100)
    dealer_id = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.name
