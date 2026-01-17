from django.shortcuts import render
from gastos import utils

def index(request):

    contexto = {}

    if request.method == 'POST':
        texto = request.POST['gastos']

        if texto.strip() == "":
            contexto['error'] = "El Campo No Debe Estar Vacio"
        else:

            try:

                mostrar_calculos = utils.calcular_gastos(texto)
            
                contexto['total'] = mostrar_calculos[0]
                contexto['cantidad'] = mostrar_calculos[1]
                contexto['promedio'] = mostrar_calculos[2]

            except ValueError:
                contexto['error'] = "Los Gastos Deben Separarse Solo Por Comas"
    
    return render(request, 'index.html', contexto) 

