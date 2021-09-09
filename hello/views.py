from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("<h1>Welcome to Azure - Batch 1 Training</h1>")
