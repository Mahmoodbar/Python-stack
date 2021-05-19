
from django.shortcuts import render
import random 	              
random.randint(1, 100) 	

def first(request):
    return render(request,"index.html")

def second(request):
    number = request.POST['number']
    if number >0 and number <100:
        if number == 48:
            pass
        
    return render(request,'index2.html')