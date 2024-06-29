from django.db import models


class ApiModel(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(max_length=300)
    nomer = models.IntegerField()
    def __str__(self):
        return self.name

