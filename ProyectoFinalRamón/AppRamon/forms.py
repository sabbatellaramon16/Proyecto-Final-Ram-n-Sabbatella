from django import forms
from AppRamon.models import Jugador, Equipo, Manager, Competencia

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = "__all__"

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = "__all__"

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = "__all__"

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = "__all__"