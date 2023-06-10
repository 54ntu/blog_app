from django import forms
from blog_app.models import commentModel

class blogAppCreateForm(forms.ModelForm):
    class Meta:
        fields=("comment","title")
        model=commentModel