
from django.urls import include, path
from . import views

urlpatterns = [
    path('welcome', views.welcome),
    path('disciplina', views.disciplina)

]