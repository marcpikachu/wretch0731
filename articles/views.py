from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from comments.forms import CommentForm
from .models import Article
from .forms import ArticleForm
from django.http import HttpResponse


def index(request):
    if request.method == "POST" and request.user.is_authenticated:
        form = ArticleForm(request.POST)
        article = form.save(commit=False)
        article.user = request.user
        article.save()

        messages.success(request, "新增成功")
        return redirect("articles:index")
    else:
        articles = Article.objects.order_by("-id")
        return render(request, "articles/index.html", {"articles": articles})


@login_required
def new(request):
    form = ArticleForm()
    return render(request, "articles/new.html", {"form": form})


def detail(request, id):
    if request.POST and request.user.is_authenticated:
        article = get_object_or_404(Article, pk=id, user=request.user)

        if request.POST["_method"] == "patch":
            form = ArticleForm(request.POST, instance=article)
            form.save()

            messages.success(request, "更新成功")
            return redirect("articles:detail", article.id)

        if request.POST["_method"] == "delete":
            article.delete()

            messages.warning(request, "刪除成功")
            return redirect("articles:index")
    else:
        article = get_object_or_404(Article, pk=id)
        comment_form = CommentForm()
        comments = (
            article.comment_set.select_related("user")
            .filter(deleted_at=None)
            .order_by("-id")
        )

        return render(
            request,
            "articles/detail.html",
            {
                "article": article,
                "comment_form": comment_form,
                "comments": comments,
            },
        )


@login_required
def edit(request, id):
    article = get_object_or_404(Article, pk=id, user=request.user)
    form = ArticleForm(instance=article)
    return render(
        request,
        "articles/edit.html",
        {"article": article, "form": form},
    )


@require_POST
@login_required
def like(request, id):
    # article = get_object_or_404(Article, pk=id)
    # if article.favoritearticle_set.contains(request.user):
    #     # 移除
    # else:
    #     # 新增
    return HttpResponse("123")