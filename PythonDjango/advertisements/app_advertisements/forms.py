from django.forms import ModelForm, Textarea
from .models import Advertisements
#from .models import AppAdvertisementsConfig

class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisements
        fields = ['title', 'description', 'price', 'auction', 'image',]
        #fields = '__all__' 
        #exclude = ['id', 'created_at', 'update_at', 'user']
        widgets = {
            'title': Textarea(attrs={'class':'form-control', 'rows':'1', 'style':""}),
            'description': Textarea(attrs={'class':'form-control', 'rows':'1', 'style':""}),
            'price': Textarea(attrs={'class':'form-control', 'rows':'1', 'style':""}),
            'auction': Textarea(attrs={'class':'form-control', 'rows':'1', 'style':""}),
            'image': Textarea(attrs={'class':'form-control', 'rows':'1', 'style':""}),
            
        }
        labels = {
            'title': 'Заголовок',

        }
        '''
        help_texts = {
            'title': 'Ведите название вашего товара',
        }
        '''
        error_messages = {'title': {
                'max_length': "Ваш заголовок не может быть таким длинным",
                },
                
                'price':
                {'max_digits':'Цена не может быть на столько большой'
                },               
        }
        

            


'''
from django import forms
#from django import ModelForm
from .models import Advertisements
from .validators import validate_title

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisements
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'price': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'type': 'number'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
        }
        
        field_classes = {
            'image': forms.ImageField(required=False),
            'auction': forms.BooleanField(required=False),
            'description': forms.CharField(required=False)
        }
'''