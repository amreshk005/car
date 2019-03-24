from django.db import models
from django.shortcuts import render,reverse


class Suscribe(models.Model):
    # id = models.CharField(max_length=20,primary_key=True)
    email = models.EmailField()

    def get_absolute_url(self):
        return reverse('car:index',kwargs={'id':self.id})

    def __str__(self):
        return self.email


