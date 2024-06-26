from django import forms
import datetime
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

class Registration(forms.Form):
    nickName = forms.CharField(label='Ваш никнейм',max_length=10,
                               help_text='Используйте не более 10 символов')
    dateBirth = forms.DateField(label='Дата рождения',help_text='Формат записи "ДЕНЬ"."МЕСЯЦ"."ГОД"',
                                input_formats=['%d.%m.%Y', 'iso-8601'])
    password1 = forms.CharField(label='Пароль',max_length=10,
                                widget=forms.PasswordInput,
                                help_text='Используйте не более 8 символов')
    password2 = forms.CharField(label='Повторить пароль',widget=forms.PasswordInput,
                                max_length=10)

class Enter(forms.Form):
    nickName = forms.CharField(label='Ваш никнейм',max_length=10,
                               help_text='Используйте не более 10 символов')

    password = forms.CharField(label='Пароль',max_length=10,
                                widget=forms.PasswordInput,
                                help_text='Используйте не более 8 символов')
