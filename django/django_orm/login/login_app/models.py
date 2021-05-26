from typing import Text
from django.db import models


class Users(models.Model):
    Name=models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)




def register(name,passwd):
    Users.objects.create(Name = name , password = passwd)

def getUsers():
    return Users.objects.all()

def check_user(name,passwd):
    user_name = Users.objects.filter(Name=name)
    
    if user_name == None:
        print("Flase")
        return False
    if user_name[0].password == passwd:
        print(user_name[0].Name)
        return user_name[0].Name
    return False


    
