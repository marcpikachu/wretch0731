from django.forms import ModelForm, Textarea, TextInput, CheckboxInput
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'is_published']
        labels = {
            'title': '標題',
            'content': '內文',
            'is_published': '是否發布',
        }
        widgets = {
            'title': TextInput(attrs={'class': 'input', 'placeholder': '文章標題'}),
            'content': Textarea(attrs={'class': 'textarea', 'placeholder': '文章內容'}),
            'is_published': CheckboxInput(attrs={'type': 'checkbox', 'class': 'checkbox'})
        }