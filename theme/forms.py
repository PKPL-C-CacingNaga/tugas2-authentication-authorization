from django import forms
from .models import SiteTheme

class SiteThemeForm(forms.ModelForm):
    class Meta:
        model = SiteTheme
        fields = ['bg_color', 'accent_color', 'text_color', 'highlight_color', 'surface_color']
        widgets = {
            'bg_color': forms.TextInput(attrs={'type': 'color'}),
            'accent_color': forms.TextInput(attrs={'type': 'color'}),
            'text_color': forms.TextInput(attrs={'type': 'color'}),
            'highlight_color': forms.TextInput(attrs={'type': 'color'}),
            'surface_color': forms.TextInput(attrs={'type': 'color'}),
        }
        labels = {
            'bg_color': 'Background Color',
            'accent_color': 'Accent Color',
            'text_color': 'Text Color',
            'highlight_color': 'Highlight Color',
            'surface_color': 'Surface Color',
        }
