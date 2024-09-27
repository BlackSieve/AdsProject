from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = [

            'category',
            'title',
            'text'
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if title == text:
            raise ValidationError(
                "Заголовок не должен быть идентичен содержанию."
            )

        return cleaned_data