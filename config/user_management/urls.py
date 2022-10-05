from django.urls import path
from . import views
from .views import login_view, signup_view

app_name = 'user_management'

urlpatterns = [
    path('login/', login_view, name = 'login'),
    path('signup/', signup_view, name = 'signup')
]