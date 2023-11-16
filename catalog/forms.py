from django import forms
from .models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image']

    def clean_name(self):
        name = self.cleaned_data['name'].lower()
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in forbidden_words:
            if word in name:
                raise forms.ValidationError(f"Название не может содержать запрещенное слово: {word}")

        return name

    def clean_description(self):
        description = self.cleaned_data['description'].lower()
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in forbidden_words:
            if word in description:
                raise forms.ValidationError(f"Описание не может содержать запрещенное слово: {word}")

        return description

class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['version_number', 'version_name', 'is_active']

    def __init__(self, *args, **kwargs):
        super(VersionForm, self).__init__(*args, **kwargs)