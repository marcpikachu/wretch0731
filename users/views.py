from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages


def new(request):
    return render(request, "users/new.html")


@require_POST
def create(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    password_confirmation = request.POST.get("password_confirmation")

    # 驗證所有必填欄位
    if not all([username, email, password, password_confirmation]):
        messages.error(request, "請填寫所有必填欄位")
        return redirect("users:new")

    # 驗證密碼是否相符
    if password != password_confirmation:
        messages.error(request, "密碼與確認密碼不相符")
        return redirect("users:new")

    # 驗證密碼長度
    if len(password) < 8:
        messages.error(request, "密碼至少需要 8 個字元")
        return redirect("users:new")

    # 檢查使用者名稱是否已存在
    if User.objects.filter(username=username).exists():
        messages.error(request, "此帳號名稱已被使用")
        return redirect("users:new")

    # 檢查 email 是否已存在
    if User.objects.filter(email=email).exists():
        messages.error(request, "此電子郵件已被註冊")
        return redirect("users:new")

    try:
        # 建立新使用者
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        
        # 認證信
        messages.success(request, f"歡迎加入有名小站，{username}！")
        return redirect("sessions:new")  # 導向登入頁面
        
    except Exception as e:
        messages.error(request, "註冊發生錯誤，請稍候再試")
        return redirect("users:new")