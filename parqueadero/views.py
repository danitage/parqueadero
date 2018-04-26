from django.shortcuts import render
from django.http import HttpResponse
from parqueadero.models import Propietario, Vehiculo
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView



def first_view(request):
    return render(request, 'base.html')

def propietario(request):
    propietario_list = Propietario.objects.all()
    context = {'object_list': propietario_list}
    return render(request, 'parqueadero/propietario.html', context)

def propietario_detail(request, propietario_id):
    
    propietario = Propietario.objects.get(id=propietario_id)
    context = {'object': propietario}
    return render(request, 'parqueadero/propietario_detail.html', context)

class VehiculoListView(ListView):
    model = Vehiculo


class VehiculoDetailView(DetailView):
    model = Vehiculo

class VehiculoUpdate(UpdateView):
    model = Vehiculo
    fields = '__all__'
    
    
class VehiculoCreate(CreateView):
    model = Vehiculo
    fields = '__all__'


class VehiculoDelete(DeleteView):
    model = Vehiculo
    success_url = reverse_lazy('vehiculo-list')

class PropietarioUpdate(UpdateView):
    model = Propietario
    fields = '__all__'
    
class PropietarioCreate(CreateView):
    model = Propietario
    fields = '__all__'

class PropietarioDelete(DeleteView):
    model = Propietario
    success_url = reverse_lazy('propietario-list')
