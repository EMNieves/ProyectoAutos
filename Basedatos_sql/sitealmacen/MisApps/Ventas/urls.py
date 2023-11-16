from django.urls import path
from MisApps.Ventas.views import VentasList, VentasDetail

app_name = "ventas"
urlpatterns = [
    path('', VentasList.as_view()),
    path('<int:pk>', VentasDetail.as_view()),
]