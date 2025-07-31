from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json 
from aplicaciones.formulario_egresados.models import Estado, Municipio, Parroquia # Importa los modelos desde tu_app


@require_POST
def get_municipios(request):
    try:
        data = json.loads(request.body)
        id_estado = data.get('idEstado')
        municipios = Municipio.objects.filter(estado_id=id_estado).values('id', 'nombre')
        return JsonResponse({'data': list(municipios)}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@require_POST
def get_parroquias(request):
    try:
        data = json.loads(request.body)
        id_municipio = data.get('idMunicipio')
        parroquias = Parroquia.objects.filter(municipio_id=id_municipio).values('id', 'nombre')
        return JsonResponse({'data': list(parroquias)}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)