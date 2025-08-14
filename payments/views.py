from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from dotenv import load_dotenv
import braintree
import os

load_dotenv()

PRICE_LIST = {
    "a": 10,
    "b": 50,
    "c": 100,
}


@login_required
def new(request):
    plan = request.GET.get("plan")
    AVAILABLE_PLANS = ["a", "b", "c"]
    if plan.lower() not in AVAILABLE_PLANS:
        plan = "a"

    token = gateway().client_token.generate()

    return render(
        request,
        "payments/new.html",
        {
            "plan": plan,
            "token": token,
            "price": PRICE_LIST.get(plan),
        },
    )


@require_POST
@login_required
def index(request):
    nonce = request.POST.get("nonce")
    plan = request.POST.get("plan")

    result = gateway().transaction.sale(
        {
            "amount": PRICE_LIST.get(plan),
            "payment_method_nonce": nonce,
        }
    )

    if result.is_success:
        # 後續
        messages.success(request, "交易完成")
    else:
        messages.error(request, "交易錯誤，請稍候再試")

    return redirect("articles:index")


def gateway():
    return braintree.BraintreeGateway(
        braintree.Configuration(
            environment=braintree.Environment.Sandbox,
            merchant_id=os.getenv("merchant_id"),
            public_key=os.getenv("public_key"),
            private_key=os.getenv("private_key"),
        )
    )