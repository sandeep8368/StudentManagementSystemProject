from django import forms
from app.models import studentModel


class studentForm(forms.ModelForm):
    class Meta:
        model = studentModel
        fields = ['name','email','password','phone']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'})
        }
        