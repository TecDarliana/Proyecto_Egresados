from django.shortcuts import redirect, render #, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import models
from uuid import uuid4
# from api.serializer import CamposSerializer
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
# from post.api.serializers import PostSerilizer
import requests
import json

from aplicaciones.formulario_egresados.forms import *
from aplicaciones.formulario_egresados.models import *




def datos_personales_egresado(request):

    personal_form = datos_pesonales_formModel()
    academic_form = datos_academicos_formModel()

    if request.method == 'POST':
        personal_form = datos_pesonales_formModel(request.POST)
        academic_form = datos_academicos_formModel(request.POST)

        if personal_form.is_valid() and academic_form.is_valid():
            # Guardar DatosPersonales
            datos_personales = personal_form.save()

            datos_academicos = academic_form.save(commit=False)
            datos_academicos.becario = datos_personales # Ajusta '' al nombre ForeignKey
            datos_academicos.save()

            messages.success(request, 'Registro se agregó con exito')
            # Redirigir a una página de éxito o a la misma página con un mensaje
            return redirect('form-listado.html') # Define esta URL en tu urls.py
        else:
            # Si alguno de los formularios no es válido, se mostrarán los errores en el template
            pass # Los errores se manejarán automáticamente por {{ form.as_p }} o similar

    context = {
        'personal_form': personal_form,
        'academic_form': academic_form,
    }
    return render(request, 'form-becarios.html', context)


def mi_vista(request):

    # Renderiza la plantilla 'mi_plantilla.html' con el contexto
  return render(request, 'form-listado.html')


def obtener_municipios(request, estado_id):
    municipios = Municipio.objects.filter(estado_id=estado_id).values('id', 'nombre').order_by('nombre')
    return JsonResponse(list(municipios), safe=False)


def consultar_cedula(request):
    nacionalidad = request.GET.get('nacionalidad')
    cedula = request.GET.get('cedula')

    if not nacionalidad or not cedula:
        # Devuelve JSON con un error si faltan los parámetros
        return JsonResponse({'error': "Se requieren los parámetros 'nacionalidad' y 'cedula'."}, status=400)

    url = "https://comunajoven.com.ve/api/cedula"
    params = {'nacionalidad': nacionalidad, 'cedula': cedula}
    headers = {
        'Authorization': 'Bearer faa3dc480981bbfb734839367d2c9367',
        'Accept': 'application/json'
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = json.loads(response.content.decode('utf-8-sig'))
        
        # Devuelve JSON si la petición es exitosa
        print(data)
        return JsonResponse(data, status=200, safe=True) 
        
    except requests.exceptions.HTTPError as e:
        # Devuelve JSON con un error si la API responde con un error HTTP
        return JsonResponse({'error': f"Error HTTP al consultar la API: {e}"}, status=response.status_code)
    except Exception as e:
        print(f"Error al consultar API: {e}")
        # Devuelve JSON con un error para cualquier otra excepción
        return JsonResponse({'error': str(e)}, status=500)