from django.shortcuts import render

def home(request):
    lucky_nums = [1, 2, 3, 16, 29]
    return render(request, "home.html", {"lucky": lucky_nums})

def about(request):
    return render(request, "about.html")