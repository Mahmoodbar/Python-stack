from typing import Text
from django.db import models



def register(name,email1,passwd):
    Users.objects.create(Name = name ,email=email1, password = passwd)

def getUsers():
    return Users.objects.all()

def check_user(name,email1,passwd):
    user_name = Users.objects.filter(Name=name)
    
    if user_name == None:
        print("Flase")
        return False
    if user_name[0].password == passwd:
        print(user_name[0].Name)
        return user_name[0].Name
    if user_name[0].email==email1:
        return user_name[0].email
    return False

class validator3(models.Manager):
    def validators(request,post_data):
        errors = {}
        
                # if register not in check_user:
                #   return redirect('/')

        if len(post_data['name']) < 2:
            errors['Name'] ='Name Must be at least 2 characters'

        if len(post_data['password']) <8:
            errors['password'] = ' Password must be at least 8 characters'

        return errors

class Users(models.Model):
    Name=models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = validator3()
    

    
