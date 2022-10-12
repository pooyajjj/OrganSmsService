from django.urls import path
from . import views
from .views import  login_view, signup_view, home, contact, forgetpass, api_call

app_name = 'user_management'

urlpatterns = [
    path('', home, name = 'home'),
    path('login/', login_view, name = 'login'),
    path('signup/', signup_view, name = 'signup'),
    path('contact', contact, name = 'contact'),
    path('forget_pass', forgetpass, name = 'forget password'),
    path('api', api_call, name = 'api call'),
]