from django.urls import path
from . import views

urlpatterns = [
    path('', views.pessoaView, name='pessoa-view')
]