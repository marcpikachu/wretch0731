from django.db import models
from articles.models import Article

class Comment(models.Model):
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # soft delete
    deleted_at = models.DateTimeField(null=True, db_index=True)  # Add index for faster queries on deleted_at
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=None)
