from django.contrib import admin

from django.urls import path,include
from .views import index
from .jsonvalidate import validateJson
urlpatterns = [
    path('index/',index),
    path('checkJson/',validateJson),

]

