from django import forms
from django.core.exceptions import ValidationError
from contacts.models import Contact


class ContactForm(forms.ModelForm):

 confirm_email = forms.EmailField(
      label="Confirm email",
      required=True,
  )
 class Meta:
            model = Contact
