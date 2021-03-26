from django.db import models

# Create your models here.


class Employe(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    