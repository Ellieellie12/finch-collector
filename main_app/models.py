from django.db import models

class Finch(models.Model):
  name = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name
