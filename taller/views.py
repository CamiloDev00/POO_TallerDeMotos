from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required # <-- NUEVO IMPORT
from .models import Motocicleta, Empleado
from .forms import MotocicletaForm

# Agregamos @login_required justo encima de CADA vista
@login_required
def lista_motos(request):
    motos = Motocicleta.objects.all()
    contexto = {'motos': motos}
    return render(request, 'taller/lista_motos.html', contexto)

@login_required
def registrar_moto(request):
    if request.method == 'POST':
        form = MotocicletaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_motos')
    else:
        form = MotocicletaForm()

    contexto = {'form': form}
    return render(request, 'taller/registrar_moto.html', contexto)

@login_required
def lista_empleados(request):
    empleados = Empleado.objects.select_related('usuario').all()
    contexto = {'empleados': empleados}
    return render(request, 'taller/lista_empleados.html', contexto)