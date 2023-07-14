from django import forms
from .models import Announcement
from django.core.exceptions import ValidationError

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['author', 'category', 'dateCreation', 'title', 'text']

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        if text is not None and len(text) < 50:
            raise ValidationError({
                "text": "Описание не может быть менее 50 символов."
            })

        title = cleaned_data.get("description")
        if title == text:
            raise ValidationError(
                "Текст объявления не может быть идентичен заголовку объявления"
            )

        return cleaned_data