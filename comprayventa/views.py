from django.shortcuts import render
from .models import Auto

# Create your views here.

def inicio(request):
    autosvar = Auto.objects.all()
    return render(request, 'comprayventa/html.html', {'listaAutos': autosvar})
    
def lista_autos(request):
    autosvar = Auto.objects.all()
    return render(request, 'comprayventa/IntrodelTP.html', {'listaAutos': autosvar})




#IntrodelTP.html        
