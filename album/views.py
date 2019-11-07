from django.shortcuts import render

from .models import Figuras
# Create your views here.
def index(request):	
	texto = 'style="background-color: yellow"'
	numeros = [i.numero for i in Figuras.objects.all()]
	return render(request, 'index.html', {'range':range(1,100), 'figuras':numeros, 'texto':texto})

def registro(request):
	pass

def faltantes(request):
	pass