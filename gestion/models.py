from django.db import models

# Create your models here.
class Trabajador(models.Model):
    class Meta:
        permissions = (("can_edit_worker", "edit_worker_success"),)
    solapin = models.IntegerField()
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Dosis(models.Model):
    class Meta:
        permissions = (("can_edit_dosis", "edit_dosis_success"),)
    d_prof = models.FloatField()
    d_piel = models.FloatField()
    d_crist = models.FloatField()
    d_comp = models.FloatField()
    trabajador = models.ForeignKey(Trabajador, on_delete= models.CASCADE)
    
    def __str__(self):
        return str(self.trabajador)
    
    