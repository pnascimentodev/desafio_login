from django.contrib import admin
from django.urls import path
from autenticacao import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('registrar/', views.registrar, name='registrar'),
    path('menu/', views.menu, name='menu'),
]