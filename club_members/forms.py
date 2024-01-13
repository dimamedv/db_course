from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    pdf_file = forms.FileField(label='PDF файл')

    class Meta:
        model = Document
        fields = ['title', 'pdf_file']
