from django import forms
from django.core.exceptions import ValidationError

from .models import Announcement, Response


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['category', 'title', 'text']

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        if text is not None and len(text) < 50:
            raise ValidationError({
                "text": "Описание не может быть менее 50 символов."
            })

        title = cleaned_data.get("title")
        if title == text:
            raise ValidationError(
                "Текст объявления не может быть идентичен заголовку объявления"
            )

        return cleaned_data

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('text', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'