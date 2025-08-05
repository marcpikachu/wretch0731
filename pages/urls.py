from .views import about, home, contact
# 等同於 from . import views 
from django.urls import path

urlpatterns = [
    path("about/", about),
    path("contact/", contact),
    path("", home),
]