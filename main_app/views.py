from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Finch:
  def __init__(self, name, color, description, age):
    self.name = name
    self.color = color 
    self.description = description
    self.age = age

finches = [
  Finch('Maggie', 'blue', 'quiet', 5),
  Finch('Lolo', 'pink', 'loud', 7),
  Finch('Sue', 'black', 'quiet', 3),
  Finch('Fancy', 'green', 'quiet', 2),
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finch_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })