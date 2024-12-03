from django import forms


class InsertarForm(forms.Form):
    solapin = forms.IntegerField(label= 'Solapin', required=True)
    name = forms.CharField(label= 'Nombre', max_length=200, required = True)

    
class Insertar_dosisForm(forms.Form):
    trabajador = forms.IntegerField(label = 'Trabajador', required = True)
    dosis_prof = forms.FloatField(label = 'Hp(10)', required = True)
    dosis_piel = forms.FloatField(label = 'Hp(0.07)', required = True)
    dosis_crist = forms.FloatField(label = 'Hp(3)', required = True)
    dosis_comp = forms.FloatField(label = 'E(50)', required = True)
    
