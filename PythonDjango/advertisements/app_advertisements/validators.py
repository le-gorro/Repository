#¥
#from django import forms
from django.core.exceptions import ValidationError



def validate_title(value):
    if value.startswith('?'):
        #raise ValidationError(_("Название объявления не может начинатся с '?'")) заголовок не может начинаться с вопросительного знака
        #raise ValidationError('Invalid value: %(value)s', code='invalid', params={'value': '?'},)
        return False, "Название объявления не может начинатся с '?'"
    return (True,)
    
