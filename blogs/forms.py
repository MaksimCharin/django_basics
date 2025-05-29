from django import forms
from .models import BlogMessage


class BlogMessageForm(forms.ModelForm):
    class Meta:
        model = BlogMessage
        fields = ['title', 'description', 'preview', 'is_published']

    def __init__(self, *args, **kwargs):
        super(BlogMessageForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название темы'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите текст сообщения'})
        self.fields['preview'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_published'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})
