from django.shortcuts import redirect, render
from .models import Disco
from .forms import UsuarioForm

# Create your views here.
def catalogo(request):
    busqueda = request.GET.get('busqueda', '')
    if busqueda:
        disco_list = Disco.objects.filter(nombre__icontains=busqueda)
    else:
        disco_list = Disco.objects.all()
    
    context = {
        "message": "Encuentra los mejores discos de vinilo para tu colección",
        "discos": disco_list,
        "busqueda": busqueda,
    }
    return render(request, 'mymusicstore/catalogo.html', context)


def registrarusuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('Main:inicio')
    else:
        form = UsuarioForm()

    return render(request, 'mymusicstore/registrarusuario.html', {'form': form})