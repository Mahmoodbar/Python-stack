from django.shortcuts import render,redirect, HttpResponse
from . import views


def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1

    context = {
        'counter' : request.session['count']

        }
    return render(request,"index.html",context)

def destroy(request):
    del request.session['count']
    return redirect("/")
# def returncount(request):
    
#     return redirect('',context)