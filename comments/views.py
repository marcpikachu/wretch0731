from django.shortcuts import redirect, get_object_or_404
from .forms import CommentForm
from articles.models import Article
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Comment


@require_POST
def create(request, id):
    article = get_object_or_404(Article, pk=id)

    form = CommentForm(request.POST)
    comment = form.save(commit=False)
    comment.article = article
    comment.save()

    messages.success(request, "新增留言成功")
    return redirect("articles:detail", article.id)


@require_POST
def delete(request, id):
    comment = get_object_or_404(Comment, pk=id)
    comment.delete()

    messages.warning(request, "刪除成功")
    return redirect("articles:detail", comment.article_id)