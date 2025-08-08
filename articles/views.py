from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Article
from .forms import ArticleForm



def index(request):
    if  request.method == "POST":
        form = ArticleForm(request.POST)
        form.save()
        # title = request.POST.get("title")
        # content = request.POST.get("content")
        # is_published = request.POST.get("is_published") == "on"
        # Article.objects.create(title=title, content=content, is_published=is_published)


        messages.success(request, "新增成功")
        return redirect("articles:index")
    else:
        articles = Article.objects.order_by("-id")

        return render(request, "articles/index.html", {"articles": articles})


def new(request):
    form = ArticleForm()
    return render(request, "articles/new.html", {"form": form})


def detail(request, id):
    article = get_object_or_404(Article, pk=id)

    if request.POST:
        if request.POST["_method"] == "patch":
            form = ArticleForm(request.POST, instance=article)
            form.save()
            # article.title = request.POST.get("title")
            # article.content = request.POST.get("content")
            # article.is_published = request.POST.get("is_published") == "on"
            # article.save()

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
    form = ArticleForm(instance=article)
    return render(request, "articles/edit.html", {"article": article, "form": form})