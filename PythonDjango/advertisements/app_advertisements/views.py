from urllib import request
from django.shortcuts import render, redirect
from .models import Advertisements
from .forms import AdvertisementForm
from django.urls import reverse
from .validators import validate_title
#from django.http import HttpResponse #return HttpResponse('успех')

def index(request):
    advertisements = Advertisements.objects.all()
    context = {'advertisements':advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):#"заголовок не может начинаться с вопросительного знака"
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            name = validate_title(form.cleaned_data["title"])
            if name[0]:
                advertisements = Advertisements(**form.cleaned_data)
                advertisements.user = request.user
                advertisements.save()
                index(request)
                #url = reverse('index.html')
                #return redirect(url)
                return index(request)
            else:
                context = {'error': name[1]}       
                return render(request, 'error.html', context)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def error(request):
    #error = Advertisements.objects.all()
    #context = {'error':error}
    context = {'error': request[1]}
    return render(request, 'error.html', context)
# Create your views here.
