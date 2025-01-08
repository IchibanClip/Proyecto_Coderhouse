from django.shortcuts import render
from .models import Disco, DiscoDestacado

# Create your views here.
def tienda_vinilos(request):
    disco_list = Disco.objects.all()
    discoDestacado_list = DiscoDestacado.objects.all()
    
    context = {
        "message": "Encuentra los mejores discos de vinilo para tu coleccion",
        "discos": disco_list,
        "discosdestacados":discoDestacado_list,
    }
    return render(request, "mymusicstore/index.html", context)