from django import forms
from django.forms import ModelForm

from .models import Bb, Rubric
"""
class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric', 'kind')
"""

class BbForm(forms.ModelForm):
    title = forms.CharField(label='Название товара')
    content = forms.CharField(label='Описание', widget=forms.widgets.Textarea())
    price = forms.DecimalField(label='Цена', decimal_places=2)
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(), label='Рубрика', help_text='Не забудьте выбрать рубрику!',
                                    widget=forms.widgets.Select(attrs={'size': 8}))
    class Meta:
        model =Bb
        fields = ('title', 'content', 'price', 'rubric', 'kind')

"""
class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Пароль (повторно)')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
"""