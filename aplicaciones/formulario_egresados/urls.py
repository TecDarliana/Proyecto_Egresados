from .import views
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from aplicaciones.formulario_egresados import views

app_name ="formulario_egresados"


urlpatterns = [
    
   path('admin/', admin.site.urls),

   path('form-becarios', views.datos_personales_egresado, name='registro'),
   path('listado', views.mi_vista, name='listado'),

 #   path('', views.home, name='inicio'),
 #  path('listado', views.listado, name='listado'),
 #  path('eliminar/<int:id>', views.eliminar, name='eliminar'),
 #  path('listado/detalle/<int:id>', views.detalle, name='detalle'),
 #  path('listado/editar/<int:id>', views.editar, name='editar'),
 #  path('l',views.historico, name='historico'),
 #  path('api/', include('aplicaciones.api.urls')),
  # path('exportar_xls/', views.export_to_xls, name='export_to_xls'),

   
   # path('logout/', vistasLogin.logout ,name="logout"),
    
    # path('historico/<int:fecha_visita_id>', views.historico name='historico'),


   # path('usuarios/', vista_usuarios, name='formulario'),
   # path('formulario/', views.formulario, name='formulario'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

