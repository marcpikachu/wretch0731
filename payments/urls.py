from django.urls import path
from . import views

app_name = "payments"

# REST
urlpatterns = [
    path("new/", views.new, name="new"),
    path("", views.index, name="index"),
]