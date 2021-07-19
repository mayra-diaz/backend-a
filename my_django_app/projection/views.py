from django.shortcuts import render

def index(request):
    return render(request, 'projection/index.html')

def utec(request):
    return render(request, 'projection/index.html')
    