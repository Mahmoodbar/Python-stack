from django.core.checks import messages
from django.db import models
from django.shortcuts import render,redirect
from .models import Users
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    context = {
        'allUsers': getUsers(),
    }
    return render(request,'index.html', context)
    

def login(request):
    errors = Users.objects.validators(request.POST)
    
    if len(errors)>0:
        for v in errors.items():
            messages.error(request,v)
        return redirect('/')


    if request.method=='POST':
        if request.POST['class'] =='loginButton':
            check_user1 = check_user(request.POST['name'],request.POST['email'],request.POST['password'])
            print('**'*30,check_user1)
            if (check_user1):
                context = {
                    'user':check_user1
                }
                return render(request,'welcome.html',context)
            else:
                # if register not in check_user:
                  return redirect('/')
             
                

        if request.POST['class'] =='registerButton':
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
            print(pw_hash)      # prints something like b'$2b$12$sqjyok5RQccl9S6eFLhEPuaRaJCcH3Esl2RWLm/cimMIEnhnLb7iC'    
            # be sure you set up your database so it can store password hashes this long (60 characters)
             # make sure you put the hashed password in the database, not the one from the form!
            Users.objects.create(Name=request.POST['name'], password=pw_hash) 
            register(name = request.POST['name'], email1= request.POST['email'],passwd = request.POST['password'])
        return redirect('/')