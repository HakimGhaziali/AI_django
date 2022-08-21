



from django import forms
 

class NForm(forms.Form):
    X1 = forms.CharField(required=False)
    X2 = forms.CharField()
    X3 = forms.CharField()
    X4 = forms.CharField()
    X5 = forms.CharField()