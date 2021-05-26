from django.db import models
from django.shortcuts import render,redirect
from .models import *
def index(request):
    context = {
        'allUsers': getUsers(),
    }
    return render(request,'index.html', context)
    

def login(request):
    if request.method=='POST':
        if request.POST['class'] =='loginButton':
            check_user1 = check_user(request.POST['name'], request.POST['password'])
            print('**'*30,check_user1)
            if (check_user1):
                context = {
                    'user':check_user1
                }
                return render(request,'welcome.html',context)
            else:
                return redirect('/')
            

        if request.POST['class'] =='registerButton':
            register(name = request.POST['name'], passwd = request.POST['password'])
    return redirect('/')