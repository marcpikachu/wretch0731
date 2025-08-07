from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("new/", views.new, name="new"),
    path("<int:id>", views.detail, name="detail"),
    path("<int:id>/edit", views.edit, name="edit"),
    path("", views.index, name="index")
]