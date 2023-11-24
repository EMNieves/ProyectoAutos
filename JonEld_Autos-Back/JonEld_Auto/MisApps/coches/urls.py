from django.urls import path
from MisApps.coches.views import CochesList, CochesDetail

app_name = "coches"
urlpatterns = [
    path('', CochesList.as_view()),
    path('<int:pk>', CochesDetail.as_view()),
]