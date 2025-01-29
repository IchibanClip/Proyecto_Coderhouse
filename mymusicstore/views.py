from django.shortcuts import redirect, render, get_object_or_404
from .models import Disco, DiscoDestacado, RegistrarUsuario, Contacto
from .forms import UsuarioForm, DiscoForm, EditarPerfilForm, CambiarContrasenaForm, ContactoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
# Create your views here.

class CatalogoListView(ListView):
    model = Disco
    template_name = 'mymusicstore/catalogo.html'
    context_object_name = 'discos'

    def get_queryset(self):
        busqueda = self.request.GET.get('busqueda', '')
        if busqueda:
            return Disco.objects.filter(nombre__icontains=busqueda)
        return Disco.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Encuentra los mejores discos de vinilo para tu colección"
        context['busqueda'] = self.request.GET.get('busqueda', '')
        return context

class DiscoDetailView(DetailView):
    model = Disco
    template_name = 'mymusicstore/detalle_disco.html'
    context_object_name = 'disco'

class DiscoDestacadoDetailView(DetailView):
    model = DiscoDestacado
    template_name = 'mymusicstore/detalle_disco_destacado.html'
    context_object_name = 'discodestacado'
    
class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('/admin/login/?next=' + self.request.path)
        messages.error(self.request, 'No tienes permiso para realizar esta acción.')
        return redirect('Main:inicio')

class RegistrarDiscoCreateView(AdminRequiredMixin, LoginRequiredMixin, CreateView):
    model = Disco
    form_class = DiscoForm
    template_name = 'mymusicstore/registrardisco.html'
    success_url = '/catalogo/'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class RegistrarDiscoDestacadoCreateView(AdminRequiredMixin, LoginRequiredMixin, CreateView):
    model = DiscoDestacado
    fields = ['estado']
    template_name = 'mymusicstore/registrardiscodestacado.html'
    success_url = '/catalogo/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['discos'] = Disco.objects.all()
        return context

    def form_valid(self, form):
        disco_id = self.request.POST.get('disco_id')
        disco = Disco.objects.get(id=disco_id)
        form.instance.nombre = disco.nombre
        form.instance.precio = disco.precio
        form.instance.autor = disco.autor
        form.instance.descripcion = disco.descripcion
        form.instance.estado = form.cleaned_data['estado']

        if disco.imagen:
            image_path = default_storage.save(disco.imagen.name, ContentFile(disco.imagen.read()))
            form.instance.imagen.name = image_path

        return super().form_valid(form)

class DiscoUpdateView(AdminRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Disco
    form_class = DiscoForm
    template_name = 'mymusicstore/editar_disco.html'
    success_url = reverse_lazy('mymusicstore:catalogo')

class DiscoDeleteView(AdminRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Disco
    template_name = 'mymusicstore/eliminar_disco.html'
    success_url = reverse_lazy('mymusicstore:catalogo')

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

def contacto(request):
    return render(request, 'mymusicstore/contacto.html')


def iniciarsesion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        contrasena = request.POST.get('contrasena')
        try:
            usuario = RegistrarUsuario.objects.get(email=email)
        except RegistrarUsuario.DoesNotExist:
            messages.error(request, 'Correo electrónico no registrado.')
            return render(request, 'mymusicstore/iniciarsesion.html')

        if usuario and usuario.contrasena == contrasena:
            usuario.estado = RegistrarUsuario.Estado.ACTIVO
            usuario.save()
            request.session['usuario_id'] = usuario.id
            request.session['usuario_nombre'] = usuario.nombre
            messages.success(request, f'Bienvenido, {usuario.nombre}')
            return redirect('Main:inicio')
        else:
            messages.error(request, 'Correo electrónico o contraseña incorrectos.')
    return render(request, 'mymusicstore/iniciarsesion.html')

def cerrarsesion(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        usuario = RegistrarUsuario.objects.get(id=usuario_id)
        usuario.estado = RegistrarUsuario.Estado.INACTIVO
        usuario.save()
        del request.session['usuario_id']
        del request.session['usuario_nombre']
    return redirect('Main:inicio')

def registrarusuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario_registrado = form.save()

            usuario_django = User.objects.create_user(
                username=usuario_registrado.email,
                email=usuario_registrado.email,
                password=usuario_registrado.contrasena,
                first_name=usuario_registrado.nombre,
                last_name=usuario_registrado.apellido
            )

            grupo_usuarios_comunes = Group.objects.get(name='Usuarios comunes')
            usuario_django.groups.add(grupo_usuarios_comunes)

            return redirect('Main:inicio')
    else:
        form = UsuarioForm()
    return render(request, 'mymusicstore/registrarusuario.html', {'form': form})

@login_required(login_url='/admin/login/')
def registrardisco(request):
    if not request.user.groups.filter(name='Admin').exists():
        messages.error(request, 'No tienes permiso para realizar esta acción.')
        return redirect('Main:inicio')
    
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
    if not request.user.groups.filter(name='Admin').exists():
        messages.error(request, 'No tienes permiso para realizar esta acción.')
        return redirect('Main:inicio')

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

def detalle_disco(request, disco_id):
    disco = get_object_or_404(Disco, id=disco_id)
    return render(request, 'mymusicstore/detalle_disco.html', {'disco': disco})

def detalle_disco_destacado(request, discodestacado_id):
    discodestacado = get_object_or_404(DiscoDestacado, id=discodestacado_id)
    return render(request, 'mymusicstore/detalle_disco_destacado.html', {'discodestacado': discodestacado})

def perfil_usuario(request, usuario_id):
    usuario = get_object_or_404(RegistrarUsuario, id=usuario_id)
    return render(request, 'mymusicstore/perfil_usuario.html', {'usuario': usuario})

def editar_perfil(request, usuario_id):
    usuario = get_object_or_404(RegistrarUsuario, id=usuario_id)
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=usuario)
        password_form = CambiarContrasenaForm(request.POST)
        if form.is_valid() and password_form.is_valid():
            form.save()
            nueva_contrasena = password_form.cleaned_data.get('nueva_contrasena')
            if nueva_contrasena:
                usuario.contrasena = nueva_contrasena
                usuario.save()
            return redirect('mymusicstore:perfil_usuario', usuario_id=usuario.id)
    else:
        form = EditarPerfilForm(instance=usuario)
        password_form = CambiarContrasenaForm()
    return render(request, 'mymusicstore/editar_perfil.html', {'form': form, 'password_form': password_form})

class ContactoCreateView(CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'mymusicstore/contacto_form.html'
    success_url = '/contacto/'

def contacto(request):
    contacto = Contacto.objects.first()
    return render(request, 'mymusicstore/contacto.html', {'contacto': contacto})
