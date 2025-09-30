from django import forms
from . import models

class EmailForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'input_field', 'placeholder': 'Enter your name...'})
        self.fields['email'].widget.attrs.update({'class': 'input_field', 'placeholder': 'Enter your Email...'})
        self.fields['message'].widget.attrs.update({'class': 'textarea_field', 'placeholder': "Tell us all about your project, or at least enough to make us say, “Wow, let’s build this!”"})

    # To render the form as div
    def as_div(self):
        return super().as_div()


