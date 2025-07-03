from django import forms
from django.core.exceptions import ValidationError
from .models import Post

    
class NewsForm(forms.ModelForm):
    description = forms.CharField(min_length=0)

    class Meta:
        model = Post
        fields = ['author', 'post_type', 'categories', 'title', 'text',]

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("description")
        name = cleaned_data.get("title")

        if name == description:
            raise ValidationError("Описание не должно быть идентично названию.")

        return cleaned_data