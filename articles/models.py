from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(null=True)
    is_published = models.BooleanField(default=False, null=False)
    user = models.ForeignKey(
        User,
        default=None,
        null=True,
        on_delete=models.SET_NULL,
    )
    likers = models.ManyToManyField(
        User,
        related_name="liked_articles",
        through="FavoriteArticle",
    )

    def __str__(self):
        return self.title


class FavoriteArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)