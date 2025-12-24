
from django.urls import path
from AppRamon import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.inicio, name="Inicio"),   # Nuestra primer view
    path('cursos/', views.cursos, name="Competencias"),
    path('profesores/', views.profesores, name="Managers"),
    path('estudiantes/', views.estudiantes, name="Jugadores"),
    path('entregables/', views.entregables, name="Equipos"),
    path('buscar/', views.buscar_resultados, name='buscar_resultados'),

    # Detalles
    path('jugador/<int:id>/', views.detalle_jugador, name='detalle_jugador'),
    path('equipo/<int:id>/', views.detalle_equipo, name='detalle_equipo'),
    path('competencia/<int:id>/', views.detalle_competencia, name='detalle_competencia'),
    path('manager/<int:id>/', views.detalle_manager, name='detalle_manager'),

    path('login/', auth_views.LoginView.as_view(template_name='AppRamon/login.html'), name='login'),
    path(
    'salir/',
    auth_views.LogoutView.as_view(next_page='Inicio', http_method_names=['get', 'post']),
    name='logout'
),
     path('registro/', views.registro, name='registro'),

    path('crear-jugador/', views.crear_jugador, name='crear_jugador'),
    path('crear-equipo/', views.crear_equipo, name='crear_equipo'),
    path('crear-manager/', views.crear_manager, name='crear_manager'),
    path('crear-competencia/', views.crear_competencia, name='crear_competencia'),

    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de_mi'),
]