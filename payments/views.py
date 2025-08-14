from django.shortcuts import render


def new(request):
    plan = request.GET.get("plan")
    AVAILABLE_PLANS = ["a", "b", "c"]
    if plan.lower() not in AVAILABLE_PLANS:
        plan = "a"

    return render(request, "payments/new.html", {"plan": plan})


def index(request):
    pass