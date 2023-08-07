from django.shortcuts import render, redirect
from .forms import formularioResidente, formularioInvitado, formularioEmpleados
from .models import Residente, Sector, Empleados, Invitado
from django.contrib import messages

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='base.html',
        context=contexto,
    )
    return http_response

def form_Socios(request):
    if request.method == 'POST':
        formulario = formularioResidente(request.POST)
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            
            residente = Residente(nombre=informacion['nombre'],
                                 edad=informacion['edad'], 
                                 direccion=informacion['direccion'], 
                                 email=informacion['email'], 
                                 telefono=informacion['telefono'], 
                                 dni=informacion['dni'],
                                 genero=informacion['genero'])
            residente.save()
            
            # Mensaje de éxito 
            messages.success(request, f'Se ha guardado el residente "{residente.nombre}" correctamente.')
            
            
            # Redireccionar a la misma página para evitar reenvío del formulario
            return redirect('formularioSocios')
            
    else:
        formulario1 = formularioResidente()
        
    return render(request, 'Socios.html', {'formulario1': formulario1})



def form_invitado(request):
    if request.method == 'POST':
        formulario_inv = formularioInvitado(request.POST)
        
        if formulario_inv.is_valid():
            informacion = formulario_inv.cleaned_data
            
            invitado = Invitado(nombre=informacion['nombre'],
                                apellido=informacion['apellido'],
                                telefono=informacion['telefono'],
                                residente=informacion['residente'])
            invitado.save()
           
           # Mensaje de éxito 
            messages.success(request, f'Se ha guardado el invitado "{invitado.apellido}, {invitado.nombre}" correctamente. {invitado.residente}')
            
            
                # Redireccionar a la misma página para evitar reenvío del formulario
            return redirect('formularioInvitado')
            
    else:
        formulario2 = formularioInvitado()
        
    return render(request, 'invitado.html', {'formulario2': formulario2})


def form_Empleados(request):
    if request.method == 'POST':
        formulario_Empleados = formularioEmpleados(request.POST)
        
        if formulario_Empleados.is_valid():
            informacion = formulario_Empleados.cleaned_data
            
            miembroEmpleados = Empleados(   nombre=informacion['nombre'],
                                    sector=informacion['sector'],
                                    telefono=informacion['telefono'])
            miembroEmpleados.save()
            
            # Mensaje de éxito
            messages.success(request, f'Se ha guardado el miembro "{miembroEmpleados.nombre}" correctamente.')
            
            # Redireccionar a la misma página para evitar reenvío del formulario
            return redirect('formularioEmpleados')
            
    else:
        formulario3 = formularioEmpleados()
        
    return render(request, 'Empleados.html', {'formulario3': formulario3})

def mostrar_sectores(request):
    # Obtener todos los sectores
    sectores = Sector.objects.all()

    # Crear una lista de trabajadores asociados a cada sector
    sectores_con_trabajadores = []
    for sector in sectores:
        trabajadores = Empleados.objects.filter(sector=sector)
        sectores_con_trabajadores.append({'sector': sector, 'trabajadores': trabajadores})

    return render(request, 'sectores.html', {'sectores_con_trabajadores': sectores_con_trabajadores})


def busqueda_resultados(request):
    if request.method == 'POST':
        palabra_clave = request.POST.get('palabra_clave', '')

        # Realizar las consultas para obtener los resultados de la búsqueda
        resultados_Socios = Residente.objects.filter(nombre__icontains=palabra_clave)
        resultados_sectores = Sector.objects.filter(nombre__icontains=palabra_clave)
        resultados_Empleados = Empleados.objects.filter(nombre__icontains=palabra_clave)

        return render(request, 'busqueda_resultados.html', {
            'palabra_clave': palabra_clave,
            'resultados_Socios': resultados_Socios,
            'resultados_sectores': resultados_sectores,
            'resultados_Empleados': resultados_Empleados,
        })
    else:
        return render(request, 'busqueda_resultados.html')
