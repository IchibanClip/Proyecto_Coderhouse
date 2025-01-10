from django.shortcuts import render
from mymusicstore.models import Disco, DiscoDestacado

# Create your views here.
def inicio(request):
    disco_list = Disco.objects.all()
    discoDestacado_list = DiscoDestacado.objects.all()
    
    context = {
        "message": "Encuentra los mejores discos de vinilo para tu coleccion",
        "discos": disco_list,
        "discosdestacados": discoDestacado_list,
    }
    return render(request, "Main/inicio.html", context)
