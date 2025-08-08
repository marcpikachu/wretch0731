from django.forms import ModelForm, Textarea
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '評論內容',
        }
        widgets = {
            'content': Textarea(attrs={'class': 'textarea', 'placeholder': '評論內容'}),
        }