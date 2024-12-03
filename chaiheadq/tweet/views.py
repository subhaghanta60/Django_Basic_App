from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'index.html')


def username(request):
    users = User.objects.all()
    for user in users:
        return HttpResponse(f"{user.username} {user.email}")

    return ""