from django.urls import path
from MisApps.Clientes.views import ClientesList, ClientesDetail

app_name = "clientes"
urlpatterns = [
    path('', ClientesList.as_view()),
    path('<int:pk>', ClientesDetail.as_view()),
]