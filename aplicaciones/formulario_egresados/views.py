from django.shortcuts import redirect, render #, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import models
from uuid import uuid4
# from api.serializer import CamposSerializer
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
# from post.api.serializers import PostSerilizer

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