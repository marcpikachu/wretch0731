from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(null=True)

# 1. 編輯 models.py
# 2. 執行 uv run python manage.py makemigrations APP_NAME
# 3. 檢查 uv run python manage.py sqlmigrate APP_NAME 編號
# 4. 執行 uv run python manage.py migrate APP_NAME
# 5. 看資料表是否產生