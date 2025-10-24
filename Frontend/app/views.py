from django.shortcuts import render
import requests


def index(request):
    return render(request, 'index.html')

def subirConfig(request):
    return render(request, 'subirConfig.html')
