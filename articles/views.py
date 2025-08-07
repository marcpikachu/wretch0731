from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

def index(request):
    if request.POST:
        title = request.POST['title']
        content = request.POST['content']
        Article.objects.create(title=title, content=content)
        return redirect("articles:index")
    else:
        articles = Article.objects.order_by("-id")
        return render(request,
                      "articles/index.html",
                      {"articles": articles})

def new(request):
    return render(request, "articles/new.html")

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, "articles/detail.html", {"article": article})