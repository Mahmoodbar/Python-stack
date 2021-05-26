from django.db import models

class Book(models.Model):
    title= models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now=True)
    notes = models.CharField(max_length=255)
    # authors = models.ForeignKey(Author,related_name="id1",on_delete=models.CASCADE)



class Author(models.Model):
    first_name= models.CharField(max_length=255)
    last_name =models.CharField(max_length=255)
    books = models.ForeignKey(Book, related_name="auts",on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now=True)
    

def check_book(num):
    # fbook = Author.objects.filter(id=int(num))
    cbook = Book.objects.filter(id= int(num))
    # print(cbook[0].title)
    return cbook[0]
    