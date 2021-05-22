
from typing import Text
from django.shortcuts import render
import random 	        

num = random.randint(1, 100)

def first(request):
    return render(request,"index.html")

def second(request):
    
    number =
    if number > 0 and number < 100:
        if number == num:
            # num = random.randint(1, 100)
            s = num , ' was the number!'
            context = {
                'color' : 'green',
                'text': s
            }
            return render(request, 'index2.html', context)
        elif number > num:
            context = {
                'color' : 'red',
                'text': 'Too High'
            }
            return render(request, 'index2.html', context)
        else:
            context = {
                'color' : 'red',
                'text' : 'Too Low'
            }
            return render(request, 'index2.html', context)
    
        
    return render(request,'index.html')