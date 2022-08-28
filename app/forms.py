

from django import forms
 

GEEKS_CHOICES =(
    ("EURUSD", "EURUSD"),
    ("EURCAD", "EURCAD"),
    ("USDCAD", "USDCAD"),
    ("AUDUSD", "AUDUSD"),
    ("GBPUSD", "GBPUSD"),
)
  


class CForm(forms.Form):

    Form_field =forms.ChoiceField(choices = GEEKS_CHOICES)
         


