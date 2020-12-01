from django.urls import path
from .views import *

urlpatterns = [
path('',home, name = 'index'),
path('graficas/',graficas, name = 'graficas'),
path('contador/',contador, name = 'contador'),
path('registros/',registros, name = 'registros'),
path('<slug:slug>/',detallePost, name = 'detalle_post'),
]
#urlpatterns = [
#path('contador/',home, name = 'contador'),
#]