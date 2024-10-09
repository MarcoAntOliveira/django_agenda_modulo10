from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                    "class" : "class a - class b",
                    "placeholder" :"Escreva Aqui",
                }
        ),
        label = 'primeiro nome ',
        help_text = 'texto de ajuda para o usuario',
    )
    qualquer = forms.CharField(
        widget = forms.TextInput(
            attrs={
                    "class" : "class a - class b",
                    "placeholder" :"Escreva Aqui",
                }
        ),
        label = 'eae ',
        help_text = 'texto de ajuda para o usuario',
    )
    
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        """self.fields['first_name'].widget.attrs.update({
            "placeholder" :"Iso veio do init"
        })
            """
            
    class Meta:
        model = models.Contact
        fields = (
                'first_name', 'last_name','phone',
                )
        
    """ widgets = {
            'first_name':forms.TextInput(
                attrs={
                    "placeholder" :"Escreva Aqui",
                }
            )
            
        }"""
    def clean(self):
        cleaned_data = self.cleaned_data
        self.add_error(
            None,
            ValidationError(
                'mensagem de error',
                code= 'invalid'
            )
        )
        
        self.add_error(
            None,
            ValidationError(
            'mensagem de error2',
                code= 'invalid'
            )
        )
        
        
        return super().clean()   