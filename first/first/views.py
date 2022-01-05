from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    #return HttpResponse("Welcome to DataBeat")
    return render(request,'home.html')
