from django.shortcuts import render
import braintree


def new(request):
    plan = request.GET.get("plan")
    AVAILABLE_PLANS = ["a", "b", "c"]
    if plan.lower() not in AVAILABLE_PLANS:
        plan = "a"

    # token
    gateway = braintree.BraintreeGateway(
        braintree.Configuration(
            environment=braintree.Environment.Sandbox,
            merchant_id="",
            public_key="",
            private_key="",
        )
    )
    token = gateway.client_token.generate()

    return render(
        request,
        "payments/new.html",
        {
            "plan": plan,
            "token": token,
        },
    )


def index(request):
    pass