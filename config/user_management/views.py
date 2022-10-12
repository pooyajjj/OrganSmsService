from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import SignUpForm


def home(request):
    return render (request, 'tmp/index.html')




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        else:
            return redirect('/../signup/')

    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'tmp/login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print("-----")
        print("form.is_valid():", form.is_valid(), form.errors)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/../login/')
        else :
            return redirect('/../no/')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'tmp/signup.html', context)


def forgetpass(request):
    pass


def contact(request):
    pass


def api_call(request):
    pass