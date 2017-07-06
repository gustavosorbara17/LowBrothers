from django.shortcuts import render
from .models import Auto

# Create your views here.

def post_list(request):
    autosvar = Auto.objects.all()
    return render(request, 'comprayventa/html.html', {'listaAutos': autosvar})


        
