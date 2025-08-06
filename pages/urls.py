# from .views import about, home, contact
from . import views 
from django.urls import path

app_name = "pages"

urlpatterns = [
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("", views.home, name="home"),
]