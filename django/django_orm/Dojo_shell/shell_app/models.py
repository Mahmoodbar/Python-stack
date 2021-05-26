from django.db import models


class dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now=True)
    

class ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(dojo,related_name="donin",on_delete=models.CASCADE)


