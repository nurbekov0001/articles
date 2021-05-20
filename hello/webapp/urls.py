from django.urls import path
from webapp.views import client_view

app_name = "client"

urlpatterns = [
    path('calculator/', client_view, "name=calculator")
]