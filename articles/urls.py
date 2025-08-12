from django.urls import path
from . import views
from comments import views as comment_views

app_name = "articles"

urlpatterns = [
    path("new/", views.new, name="new"),
    path("<int:id>/edit", views.edit, name="edit"),
    path("<int:id>/comments", comment_views.create, name="create_comment"),
    path("<int:id>/like", views.like, name="like"),
    path("<int:id>", views.detail, name="detail"),
    path("", views.index, name="index"),
]