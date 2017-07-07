from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'listado/', views.inicio),
        url(r'^$', views.lista_autos),
    ]
