from django.urls import path
from MisApps.cliente.views import ClienteList, ClienteDetail

app_name = "clientes"
urlpatterns = [
    path('', ClienteList.as_view()),
    path('<int:pk>', ClienteDetail.as_view()),
]