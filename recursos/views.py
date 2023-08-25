from django.shortcuts import render
from .models import Person
# Create your views here.
def validar_fecha(fecha_texto):
    from datetime import datetime
    try:
        return datetime.strptime(fecha_texto, "%Y-%m-%d")
    except:
        return False

def v_index(request):

    consulta = Person.objects.all().order_by('firstname')

    filtro_firstname = request.GET.get("firstname", False)
    if filtro_firstname:
        consulta = consulta.filter(firstname__istartswith = filtro_firstname)

    filtro_start = validar_fecha(request.GET.get('startdate', False))
    filtro_end = validar_fecha(request.GET.get('enddate', False))
    
    if filtro_start and filtro_end:
        consulta = consulta.filter(modifieddate__range = (filtro_start, 
            filtro_end))


    p20 = consulta[:20]

    context = {
        'personas': p20,
        'f_firstname': filtro_firstname if filtro_firstname else ''
    }
    return render(request, 'index.html', context)