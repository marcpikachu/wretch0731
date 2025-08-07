from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Article


def index(request):
    if request.POST:
        title = request.POST["title"]
        content = request.POST["content"]
        Article.objects.create(title=title, content=content)

        messages.success(request, "新增成功")
        return redirect("articles:index")
    else:
        articles = Article.objects.order_by("-id")
        return render(request, "articles/index.html", {"articles": articles})


def new(request):
    return render(request, "articles/new.html")


def detail(request, id):
    article = get_object_or_404(Article, pk=id)

    if request.POST:
        if request.POST["_method"] == "patch":
            article.title = request.POST["title"]
            article.content = request.POST["content"]
            article.save()

            messages.success(request, "更新成功")
            return redirect("articles:detail", article.id)

        if request.POST["_method"] == "delete":
            article.delete()

            messages.warning(request, "刪除成功")
            return redirect("articles:index")
    else:
        return render(request, "articles/detail.html", {"article": article})


def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, "articles/edit.html", {"article": article})