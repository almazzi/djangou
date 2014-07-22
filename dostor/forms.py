from django import forms
from dostor.models import Dostor
from django.core.exceptions import ValidationError

class DostorForm(forms.ModelForm):

    confirm_email = forms.EmailField(
        label="email confirm",
        required=True,

    )
    class Meta:
        model = Dostor

    def __init__(self,*args,**kwargs):
        if kwargs.get('instance'):
            email = kwargs['instance'].email
            kwargs.setdefault('initial', {})['confirm_email'] = email

        return super(DostorForm,self).__init__(*args,**kwargs)

    def clean(self):
        if (self.cleaned_data.get('email') != self.cleaned_data.get('confirm_email')):
            raise ValidationError("dal kelbei jatat eki email");
        confirm_email= "";
        return self.cleaned_data


