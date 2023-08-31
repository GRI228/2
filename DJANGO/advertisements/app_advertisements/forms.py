from django import forms
from .models import Advertisement

class AdvertisementForm(forms.ModelForm):

    class Meta:
        model = Advertisement
        fields = '__all__'
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'price': 'Цена',
            'auction': 'Торг',
            'image': 'Изображение'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and title[0] == '?':
            raise forms.ValidationError("Заголовок не может начинаться с вопросительного знака")
        return title