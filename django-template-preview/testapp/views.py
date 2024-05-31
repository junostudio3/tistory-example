from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'testapp/index.html')

from django.templatetags.static import static

def index2(request):
  imageLink:str = static('sample.png')

  context = {
    'image': imageLink,
  }

  return render(request, 'testapp/index2.html', context)