from django.shortcuts import render,HttpResponse ,redirect
from .models import Book
from .models import *

# Create your views here.
def index(request):
    context = {
        'zbooks' : Book.objects.all()
    }
    return render(request,'index.html',context)

def second(request):
    if request.method=='POST':
        if request.POST['class']== 'adding':
            Book.objects.create(title=request.POST['title'],desc=request.POST['desc'])
        
        if request.POST['class']=='viewing':
            return redirect('books/num')
    return redirect('/')

def view(request,num):
    check_book1=check_book(num)
  
    if (check_book1):
        context = {
        'dbooks' : check_book1
        
      }

        return render(request,'book.html' ,context)