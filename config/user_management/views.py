from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .models import user
# Create your views here.

def Login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, Username=username, Password=password)
    if user.is_valid():
        return redirect('/organsmspanel')
        
