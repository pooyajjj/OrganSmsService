from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import View



def login_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('/ok/')
        else :
            return redirect('/../signup/')
    
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'tmp/login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('/ok/')
        else :
            return redirect('/../no/')
    return render(request, 'tmp/signup.html')

# class base signup
# class signup_view(View):
#     def get(sefl, request):
#         return render(request, 'tmp/signup.html',{'form': UserCreationForm()})

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             user.save()
#             login(request, user)
#             return redirect('nice/')
#         else :
#             return redirect ('/../fuck/')
#         # return render(request, 'tmp/signup.html', {'form': UserCreationForm()})


