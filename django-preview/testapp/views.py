from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static

def index(request):
    text:str = "<head></head><body><img src=" + static("sample.png") + "></body>"
    return HttpResponse(text)
