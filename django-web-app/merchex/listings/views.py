from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

def hello(request):
    bands = Band.objects.all()
    listing = Listing.objects.all()
    #to get the objects
    return render(request, 'listings/hello.html')

def about(request):
    return HttpResponse('<h1>About Us</h1> <p>We love merch!</p>')


