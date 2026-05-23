from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # <-- NUEVO IMPORT
from . import views

urlpatterns = [
    # 1. La raíz del sitio ('') ahora es la pantalla de Login
    path('', LoginView.as_view(template_name='taller/login.html'), name='login'),

    # 2. Ruta para cerrar sesión
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # 3. Tus rutas protegidas
    path('inventario/', views.lista_motos, name='lista_motos'),
    path('registrar/', views.registrar_moto, name='registrar_moto'),
    path('empleados/', views.lista_empleados, name='lista_empleados'),
]