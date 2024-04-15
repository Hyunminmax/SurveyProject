from django.urls import path
from .views import *

urlpatterns = [
    path('', user_view, name='user_view'),
]