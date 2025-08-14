from django.urls import path
from . import views
from articles.views import index

app_name = "pages"

urlpatterns = [
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("pricing/", views.pricing, name="pricing"),
    path("", index, name="home"),
    path("test/", views.test, name="test"),
]