from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Trabajador, Dosis
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy




# Create your views here.
def index(request):
    
    num_trabajadores = Trabajador.objects.count()
    context={
        'num_trabajadores': num_trabajadores,
        
    }
    return render(request, 'enmarcados/index.html', context=context)

def trabajadores(request):
    trabajadores = Trabajador.objects.all()
    return render(request, 'trabajadores.html', {'trabajadores': trabajadores})

@login_required
def dosis(request):
    dosis = Dosis.objects.all()
    return render(request, 'dosis.html', {'dosis': dosis})

"""def insertar(request):
    if request.method == 'GET':   
        return render(request, 'insertar.html', {'form': InsertarForm()})
    else:
        Trabajador.objects.create(solapin = request.POST.get('solapin'), name = request.POST.get('name'))
        return redirect('trabajadores')"""
"""@login_required    
def insertar_dosis(request):
    if request.method == 'GET':
       return render(request, 'insertar_dosis.html', {
       'form': Insertar_dosisForm()})
    else:
        Dosis.objects.create(trabajador_id= request.POST.get('trabajador'), d_prof = request.POST.get('dosis_prof'), 
                            d_piel = request.POST.get('dosis_piel'), d_crist = request.POST.get('dosis_crist'),
                            d_comp = request.POST.get('dosis_comp'))
        return redirect('dosis')"""      
"""#def editar_trabajador(request, id):
    trabajador = Trabajador.objects.get(id = id)
    if request.method == 'GET':
        form = InsertarForm(request.GET, instance = trabajador)
        contexto = {
            'form': form
            }
    else:
        form = InsertarForm(request.POST, instance = trabajador)
        contexto = {
            'form': form
            }
        if form.is_valid():
            form.save()
            return redirect('trabajadores')
    return render(request, 'insertar.html', contexto)"""
    
@login_required
def eliminar_trabajador(request, id):
    trabajador = Trabajador.objects.get(id=id)
    trabajador.delete()
    return redirect('trabajadores')

@login_required
def eliminar_dosis(request, id):
    dosis = Dosis.objects.get(id=id)
    dosis.delete()
    return redirect('dosis')   

def buscar(request):    
    
    if request.GET['bar']:
        
        trabajador = request.GET['bar']
        result = Trabajador.objects.filter(name__icontains=trabajador)
        return render(request, 'enmarcados/index.html', {'resultado':result, 'query':trabajador})
    
"""--------------------------------VISTAS BASADAS EN CLASES-------------------------------------------------"""    

class Crear_trabajador(LoginRequiredMixin,CreateView):
    model = Trabajador
    fields = ['solapin', 'name']
    success_url = reverse_lazy('trabajadores')


class Editar_trabajador(LoginRequiredMixin,UpdateView):
    
    model = Trabajador
    fields = ['solapin', 'name']
    success_url = reverse_lazy('trabajadores')

class Insertar_dosis(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('Trabajador_modificado', 'can_add_dosis')
    model = Dosis
    fields = '__all__'
    success_url = reverse_lazy('dosis')
    

class Editar_dosis(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    
    permission_required = ('edit_dosis_success')
    model = Dosis
    fields = '__all__'
    success_url = reverse_lazy('dosis')

#------------------------------------------------------------Auteticacion----------------------------------------------------------
