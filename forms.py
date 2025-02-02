from django import forms
from .models import Dataset

#class DatasetForm(forms.ModelForm):
 #   class Meta:
#        model = Dataset
#        fields = ['name', 'folder']
#from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label="Upload an image of a coffee leaf")
