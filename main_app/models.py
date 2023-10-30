from django.db import models
from django.urls import reverse

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Finch(models.Model):
  name = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("finch-detail", kwargs={"finch_id": self.id})
  
class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(max_length=1)