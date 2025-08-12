from django.shortcuts import render
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as logout_user
from django.http import HttpResponse


def new(request):
    return render(request, "sessions/new.html")


@require_POST
def create(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(
        username=username,
        password=password,
    )

    if user:
        login(request, user)
        messages.success(request, "已登入")
        return redirect("articles:index")
    else:
        messages.error(request, "登入失敗")
        return redirect("sessions:new")


@require_http_methods(["DELETE"])
def logout(request):
    logout_user(request)
    return render(request, "shared/navbar.html")