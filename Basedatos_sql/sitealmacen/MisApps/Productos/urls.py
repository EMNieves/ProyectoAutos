from django.urls import path
from MisApps.Productos.views import ProductoList, ProductoDetail

app_name = "producto"
urlpatterns = [
    path('', ProductoList.as_view()),
    path('<int:pk>', ProductoDetail.as_view()),
]