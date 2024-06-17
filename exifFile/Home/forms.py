from django import forms
from .models import ImageUpload

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model=ImageUpload
        fields=[
            'image'
        ]
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control form-large '}),
        }   
        labels = {
            'image': '',  # Remove the label
        }
