from django.shortcuts import render
from .models import Person
# Create your views here.
def v_index(request):

    consulta = Person.objects.all().order_by('firstname')

    filtro_firstname = request.GET.get("firstname", False)
    if filtro_firstname:
        consulta = consulta.filter(firstname__istartswith = filtro_firstname)


    p20 = consulta[:20]

    context = {
        'personas': p20,
        'f_firstname': filtro_firstname
    }
    return render(request, 'index.html', context)