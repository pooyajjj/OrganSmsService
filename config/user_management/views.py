from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

# Create your views here.


class Login(View):
    def get(self, request):
        return render(request, 'tmp/login.html', {'form': AuthenticationForm })

    def post(self, request):
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username = form.cleaned_data.get('username'),
                password = form.cleaned_data.get('password')
            )
        return redirect('/organsmspanel')
        
