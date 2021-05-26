
from shell_app.models import dojo
from django.shortcuts import render, HttpResponse ,redirect
from .models import ninja, dojo 
from . import models

def index(request):
    context ={
      'all_dojo' : dojo.objects.all()
    }

    return render(request,'index.html',context)

def second(request):
   
    if request.method=='POST' and request.POST['class']=='dojo':

        dojo.objects.create(name = request.POST['name'], city = request.POST['city'], state = request.POST['state'])
    

    if request.method=='POST' and request.POST['class']=='ninja': 

        ninja.objects.create(first_name = request.POST['first'], last_name = request.POST['last'], dojo = dojo.objects.get(name=request.POST['optiondojo']))

    return redirect('/')
