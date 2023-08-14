from django.shortcuts import render
from .models import Advertisements
#from django.http import HttpResponse #return HttpResponse('успех')

def index(reguest):
    advertisements = Advertisements.objects.all()
    context = {'advertisements':advertisements}
    return render(reguest, 'index.html', context)

def top_sellers(reguest):
    return render(reguest, 'top-sellers.html')

def advertisement_post(reguest):
    return render(reguest, 'advertisement-post.html')

def register(reguest):
    return render(reguest, 'register.html')

def login(reguest):
    return render(reguest, 'login.html')

def profile(reguest):
    return render(reguest, 'profile.html')
# Create your views here.
