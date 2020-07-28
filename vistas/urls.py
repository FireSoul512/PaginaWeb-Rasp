from django.urls import path

from .views import vistaClass, vistaConf

urlpatterns = [
    path('index/', vistaClass.as_view()),
    path('configure/',vistaConf.as_view()),
]
