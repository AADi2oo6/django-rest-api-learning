from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    return HttpResponse("<h1> Hellow World :This is Students HOme page</h1>")
