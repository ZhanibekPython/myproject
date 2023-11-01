from datetime import datetime

from django import forms

from .models import Product, Author


class ProductForm(forms.Form):
    class Meta:
        forms = Product
        fields = ['name', 'photo']


class Choose_game(forms.Form):
    game = forms.ChoiceField(choices=[('C', 'Coins'), ('R', 'Random_nums')])
    attempts = forms.IntegerField(min_value=1, max_value=64, widget=forms.NumberInput(attrs={'class': 'form-control'}))


class AddAuthor(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Enter your name'}))
    surname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'Enter your surname'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    biography = forms.CharField(max_length=555, widget=forms.Textarea(attrs={'class': 'form-control'}))
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))


# class ChooseAuthor(forms.Form):
#     def get_author(self):
#
#
#     name = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))


class AddArticle(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Enter your name'}))
    body = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control'}))
    pub_date = forms.DateField(initial=datetime.utcnow, widget=forms.DateInput(attrs={'class': 'form-control'}))
    category = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Description body'}))
    view = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_publ = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    author = forms.ModelChoiceField(queryset=Author.objects.all())


class UpdateProduction(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Enter your name'}))
    description = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.DecimalField(max_digits=9, decimal_places=2,
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))
    quontity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    add_date = forms.DateField()
