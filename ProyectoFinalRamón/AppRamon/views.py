from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from AppRamon.models import Competencia, Equipo, Manager, Jugador
from AppRamon.forms import JugadorForm, EquipoForm, ManagerForm, CompetenciaForm

def inicio(request):
    return render(request, "AppRamon/inicio.html")


def cursos(request):
    competencias = Competencia.objects.all()
    return render(request, "AppRamon/cursos.html", {"cursos": competencias})


def profesores(request):
    managers = Manager.objects.all()
    return render(request, "AppRamon/profesores.html", {"profesores": managers})


def estudiantes(request):
    jugadores = Jugador.objects.all()
    return render(request, "AppRamon/estudiantes.html", {"estudiantes": jugadores})


def entregables(request):
    equipos = Equipo.objects.all()
    return render(request, "AppRamon/entregables.html", {"entregables": equipos})

def buscar_resultados(request):
    query = request.GET.get('q', '')

    jugadores = Jugador.objects.filter(
        Q(nombre__icontains=query) |
        Q(apellido__icontains=query) |
        Q(posición__icontains=query) |
        Q(equipo__icontains=query) |
        Q(nacionalidad__icontains=query)
    )

    equipos = Equipo.objects.filter(
        Q(nombre__icontains=query) |
        Q(pais__icontains=query)
    )

    competencias = Competencia.objects.filter(
        Q(nombre__icontains=query) |
        Q(pais__icontains=query)
    )

    managers = Manager.objects.filter(
        Q(nombre__icontains=query) |
        Q(apellido__icontains=query) |
        Q(equipo__icontains=query) |
        Q(nacionalidad__icontains=query)
    )

    context = {
        'query': query,
        'jugadores': jugadores,
        'equipos': equipos,
        'competencias': competencias,
        'managers': managers,
    }

    return render(request, 'AppRamon/resultados_busqueda.html', context)


def detalle_jugador(request, id):
    jugador = Jugador.objects.get(id=id)
    return render(request, "AppRamon/detalle_jugador.html", {"jugador": jugador})


def detalle_equipo(request, id):
    equipo = Equipo.objects.get(id=id)
    return render(request, "AppRamon/detalle_equipo.html", {"equipo": equipo})


def detalle_competencia(request, id):
    competencia = Competencia.objects.get(id=id)
    return render(request, "AppRamon/detalle_competencia.html", {"competencia": competencia})


def detalle_manager(request, id):
    manager = Manager.objects.get(id=id)
    return render(request, "AppRamon/detalle_manager.html", {"manager": manager})


def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("Inicio")
    else:
        form = UserCreationForm()

    return render(request, "AppRamon/registro.html", {"form": form})

@login_required
def crear_jugador(request):
    if request.method == "POST":
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Jugadores")
    else:
        form = JugadorForm()

    return render(request, "AppRamon/crear_jugador.html", {"form": form})


@login_required
def crear_equipo(request):
    if request.method == "POST":
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Equipos")
    else:
        form = EquipoForm()

    return render(request, "AppRamon/crear_equipo.html", {"form": form})


@login_required
def crear_manager(request):
    if request.method == "POST":
        form = ManagerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Managers")
    else:
        form = ManagerForm()

    return render(request, "AppRamon/crear_manager.html", {"form": form})


@login_required
def crear_competencia(request):
    if request.method == "POST":
        form = CompetenciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Competencias")
    else:
        form = CompetenciaForm()

    return render(request, "AppRamon/crear_competencia.html", {"form": form})
    
def acerca_de_mi(request):
    return render(request, "AppRamon/acerca_de_mi.html")