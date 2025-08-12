from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(null=True)
    is_published = models.BooleanField(default=False, null=False)
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.title
    