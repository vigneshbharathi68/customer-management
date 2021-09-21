# -*- coding: utf-8 -*-

# Django modules
from django.urls import path

# local modules
from . import views
from .views import (
    Customers
)

urlpatterns = [
    path('help/', Customers.as_view(), name='logout_api'),
]
