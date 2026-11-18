from django import forms
from .models import Clienti, Mendgeri, Tarifini_plan, Podchenie_nomera, JurnalSoversheniZvonkov

class ClientiForm(forms.ModelForm):
    class Meta:
        model = Clienti
        fields = '__all__'

class MendgeriForm(forms.ModelForm):
    class Meta:
        model = Mendgeri
        fields = '__all__'

class Tarifini_planForm(forms.ModelForm):
    class Meta:
        model = Tarifini_plan
        fields = '__all__'

class Podchenie_nomeraForm(forms.ModelForm):
    class Meta:
        model = Podchenie_nomera
        fields = '__all__'

class JurnalSoversheniZvonkovForm(forms.ModelForm):
    class Meta:
        model = JurnalSoversheniZvonkov
        fields = '__all__'