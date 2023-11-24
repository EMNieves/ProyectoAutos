from django.urls import path
from MisApps.marcas.views import MarcasList, MarcasDetail

app_name = "marcas"
urlpatterns = [
    path('', MarcasList.as_view()),
    path('<int:pk>', MarcasDetail.as_view()),
]