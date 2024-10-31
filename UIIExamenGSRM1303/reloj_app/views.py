from django.shortcuts import render
from .models import Reloj

# Create your views here.
def inicio_vista(request):
    
    ListadoRelojes= Reloj.objects.all()
    return render(request, "gestionarReloj.html",{"losrelojes" : ListadoRelojes})