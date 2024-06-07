from django.shortcuts import render
from django.http import HttpResponse
from .models import FruitStorage

# Create your views here.

def index(request):
  items = []

  objs = FruitStorage.objects.all()
  for obj in objs:
    items.append((str(obj.date), obj.name, str(obj.price)))

  context = {
    'items': items,
  }

  return render(request, 'testapp/index.html', context)