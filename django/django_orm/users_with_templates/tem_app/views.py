from django.db.models.fields import EmailField
from django.shortcuts import redirect, render ,HttpResponse
from .models import User

def first(request):
    context ={
        "x": User.objects.all()
    }
    return render (request,"index.html",context)

def second(request):
    User.objects.create(first_name=request.POST['first'] ,last_name=request.POST['last'], email_address=request.POST['email'], age=request.POST['age'])
    return redirect ('/')
