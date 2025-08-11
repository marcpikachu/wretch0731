from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages


def new(request):
    return render(request, "sessions/new.html")


@require_POST
def create(request):
    pass