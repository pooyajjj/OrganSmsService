from django.urls import path
from . import views
from .views import login_view

app_name = 'user_management'

urlpatterns = [
    path('login/', login_view, name = 'login'),
]