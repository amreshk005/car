from django import forms
from .models import Suscribe


class SuscribeForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Suscribe
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(SuscribeForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs\
            .update({
                'placeholder': 'your email',
                'class': 'input-text'
            })

    