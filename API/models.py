from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=15)
    age = models.IntegerField()
    city = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name