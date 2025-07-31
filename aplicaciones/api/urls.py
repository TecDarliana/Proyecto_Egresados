from django.urls import path
from . import views

urlpatterns = [
    path('get_municipios/', views.get_municipios, name='api_get_municipios'),
    path('get_parroquias/', views.get_parroquias, name='api_get_parroquias'),
]
