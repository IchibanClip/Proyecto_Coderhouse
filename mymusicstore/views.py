from django.shortcuts import redirect, render, get_object_or_404
from .models import Disco, DiscoDestacado
from .forms import UsuarioForm, DiscoForm
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='/admin/login/')
def registrardisco(request):
    if not request.user.is_staff:
        return redirect('admin:login')
    
    if request.method == 'POST':
        form = DiscoForm(request.POST)
        if form.is_valid():
            disco = form.save(commit=False)
            disco.autor = request.user
            disco.estado = Disco.Estado.BORRADOR
            disco.save()
            return redirect('mymusicstore:catalogo')
    else:
        form = DiscoForm()

    return render(request, 'mymusicstore/registrardisco.html', {'form': form})

@login_required(login_url='/admin/login/')
def registrardiscodestacado(request):
    if not request.user.is_authenticated:
        return redirect("admin:login")

    discos = Disco.objects.all()

    if request.method == "POST":
        disco_id = request.POST.get("disco")
        if disco_id:
            disco = get_object_or_404(Disco, id=disco_id)
            DiscoDestacado.objects.create(
                nombre=disco.nombre,
                precio=disco.precio,
                estado=disco.estado,
                autor=disco.autor,
            )
            return redirect("mymusicstore:catalogo")

    return render(request, "mymusicstore/registrardiscodestacado.html", {"discos": discos})
