# from .views import about, home, contact
from . import views 
from django.urls import path
from articles.views import index

app_name = "pages"

urlpatterns = [
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("", index, name="home"),
]