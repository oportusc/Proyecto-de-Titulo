from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota, MascotaDesaparecida, FormularioAdopcion
from .forms import FormularioSolicitudes,ContactoForm, MascotaForm, CustomUserCreationForm, MascotaDesaparecidaForm, FormularioAdopcionForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic import ListView, View
from .utils import render_to_pdf
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def home(request):
    queryset = request.POST.get("buscar")
    queryset2 = request.POST.get("buscar2")
    
    filtro = []
    if queryset != None and queryset != '-1':
        filtro.append(('especie' , int(queryset)))
    if queryset2 != None and queryset2 != '-1':
        filtro.append(('sexo' , int(queryset2)))

    mascotas = Mascota.objects.all()


    if len(filtro) > 0 :
        mascotas = Mascota.objects.filter(
            *filtro
    )
    data = {
        'mascotas': mascotas,
        'mensaje': "Lo sentimos no hay mascotas"
    }

    return render(request, 'app/home.html', data)




#Mascotas Desaparecidas
def mascotasDesaparecidas(request):
    queryset = request.POST.get("buscar")
    
    filtro=[]
    if queryset != None and queryset != '-1':
        filtro.append(('tipo_publicacion', queryset))

    mascotas = MascotaDesaparecida.objects.all()

    if len(filtro)>0:
        mascotas = MascotaDesaparecida.objects.filter(
            *filtro
        )

    data = {
        'mascotas': mascotas
    }
    return render(request, 'app/mascotas_desaparecidas/mascotas.html', data)

@login_required
def agregar_mascota_desaparecida(request):
    data = {
        'form': MascotaDesaparecidaForm()
    }
    if request.method =='POST':
        form = MascotaDesaparecidaForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Mascota Publicada con exito")
            return redirect(to="mascotas_desaparecidas")
        else:
            data["form"]=form
    return render(request, 'app/mascotas_desaparecidas/agregar.html', data)

@permission_required('app.view_mascotadesaparecida')
def listar_mascotas_desaparecidas(request):
    mascotas = MascotaDesaparecida.objects.all()
    data = {
        'mascotas': mascotas
    }
    return render(request, 'app/mascotas_desaparecidas/listar.html', data)

@permission_required('app.delete_mascotadesaparecida')
def eliminar_mascota_desaparecida(request, id):
    mascota = get_object_or_404(MascotaDesaparecida, id=id)
    mascota.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_mascotas_desaparecidas")


# CRUD MASCOTA
@permission_required('app.add_mascota')
def agregar_mascota(request):
    data = {
        'form': MascotaForm()
    }
    if request.method == 'POST':
        formulario =MascotaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mascota registrada")
        else:
            data["form"] = formulario
    return render(request, 'app/mascota/agregar.html', data)

@permission_required('app.view_mascota')
def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    data = {
        'mascotas': mascotas
    }
    return render(request, 'app/mascota/listar.html', data)
    
@permission_required('app.change_mascota')
def modificar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    data = {
        'form': MascotaForm(instance=mascota)
    }
    if request.method == 'POST':
        formulario = MascotaForm(data=request.POST, instance=mascota, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_mascotas")
            data["form"] = formulario
    return render(request, 'app/mascota/modificar.html', data)

@permission_required('app.delete_mascota')
def eliminar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    mascota.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_mascotas")


@permission_required('app.change_formularioadopcion')
def rechazar_solicitud(request, id):
    solicitud = get_object_or_404(FormularioAdopcion, id=id)
    solicitud.estado_solicitud = 'Rechazada'
    solicitud.save()

    messages.success(request, "Rechazada correctamente")
    return redirect(to="listar_solicitudes")

@permission_required('app.change_formularioadopcion')
def aceptar_solicitud(request, id):
    solicitud = get_object_or_404(FormularioAdopcion, id=id)
    solicitud.estado_solicitud = 'Aprobada'
    solicitud.save()
    

    messages.success(request, "Aprobada correctamente")
    return redirect(to="listar_solicitudes")


@permission_required('app.delete_formularioadopcion')
def eliminar_solicitudes(request, id):
    solicitud = get_object_or_404(FormularioAdopcion, id=id)
    solicitud.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_mascotas")

@permission_required('app.view_formularioadopcion')
def ver_rechazada(request, id):
    solicitudes = get_object_or_404(FormularioAdopcion, id=id)
    data ={
        'form': FormularioSolicitudes(instance=solicitudes)
    }
    return render(request,'app/mascota/ver_rechazadas.html',data)




@permission_required('app.view_formularioadopcion')
def ver_aprobada(request, id):
    solicitudes = get_object_or_404(FormularioAdopcion, id=id)
    data ={
        'form': FormularioSolicitudes(instance=solicitudes)
    }
    return render(request,'app/mascota/ver_aprobadas.html',data)

@permission_required('app.view_formularioadopcion')
def ver_solicitud(request, id):
    solicitudes = get_object_or_404(FormularioAdopcion, id=id)
    data ={
        'form': FormularioSolicitudes(instance=solicitudes)
    }
    return render(request,'app/mascota/ver_solicitudes.html',data)

@permission_required('app.view_formularioadopcion')
def listar_rechazadas(request):
    solicitudes = FormularioAdopcion.objects.all().order_by('-fecha_solicitud')
    data = {
        'solicitudes': solicitudes
    }
    return render(request, 'app/mascota/solicitudes_rechazadas.html', data)

@permission_required('app.view_formularioadopcion')
def listar_aprobadas(request):
    solicitudes = FormularioAdopcion.objects.all().order_by('-fecha_solicitud')
    data = {
        'solicitudes': solicitudes
    }
    return render(request, 'app/mascota/solicitudes_aprobadas.html', data)


@permission_required('app.view_formularioadopcion')
def listar_solicitudes(request):
    solicitudes = FormularioAdopcion.objects.all().order_by('-fecha_solicitud')
    data = {
        'solicitudes': solicitudes
    }
    return render(request, 'app/mascota/listar_solicitudes.html', data)


# Registro de usuario
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro exitoso")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)



#estaticos
def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        to= request.POST.get('correo')
        content = request.POST.get('mensaje')
        nombre = request.POST.get('nombre')
        asunto = request.POST.get('tipo_consulta')

        email_from = settings.EMAIL_HOST_USER

        html_content = render_to_string("app/contacto_email.html",{'asunto':asunto, 'content':content, 'nombre':nombre})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(asunto,text_content,email_from,[to, settings.EMAIL_HOST_USER])
        email.attach_alternative(html_content,"text/html")
        email.send()
        messages.success(request, "Solicitud enviada con exito uno de nuestros voluntarios se comunicara con usted.")
        return render(request,"app/nosotros.html")

    return render(request, 'app/contacto.html', data)

@login_required
def formulario_adopcion(request):
    data = {
        'form': FormularioAdopcionForm()
    }
    if request.method =='POST':
        form = FormularioAdopcionForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            nombres = form.save(commit=False)
            nombres.nombres = request.user.first_name
            nombres.save()

            apellidos = form.save(commit=False)
            apellidos.apellidos = request.user.last_name
            apellidos.save()

            to = request.user.email
            subject = "Solicitud de Adopción - Mascota Numero:" + " " + request.POST["mascota"]
            nombre = request.user.first_name +" "+ request.user.last_name
            contacto = request.POST["telefono"]
            edad = request.POST["edad"]
            tipo_vivienda = request.POST["tipo_vivienda"]
            direccion = request.POST["direccion"]
            cant_mascota = request.POST["cantidad_mascotas"]
            estado_solicitud = request.POST["estado_solicitud"]

            email_from = settings.EMAIL_HOST_USER
            
            form.save()

            html_content = render_to_string("app/solicitud_email.html",{'nombre':nombre, 'contacto':contacto, 'edad':edad, 'tipo_vivienda':tipo_vivienda, 'direccion':direccion, 'cant_mascota':cant_mascota, 'subject':subject,'estado_solicitud':estado_solicitud})

            text_content = strip_tags(html_content)
            email= EmailMultiAlternatives(subject,text_content,email_from,[to, settings.EMAIL_HOST_USER])
            email.attach_alternative(html_content,"text/html")
            email.send()
            messages.success(request, "Solicitud de adopción enviada correctamente, uno de nuestros voluntarios se comunicara con usted.")
            return render(request,"app/nosotros.html")
            
        else:
            data["form"]=form
    return render(request, 'app/mascota/form_adopcion.html', data)






def nosotros(request):
    return render(request, 'app/nosotros.html')


# Apartado PDF
class ListaMascotasListView(ListView):
    model = Mascota
    template_name = "app/mascota/reporte_mascota.html"
    context_object_name = 'mascotas'

class ListMascotasPdf(View):
    def get(self, request, *args, **kwargs):
        mascotas = Mascota.objects.all()
        data = {
            'mascotas' : mascotas,
        }
        pdf = render_to_pdf('app/mascota/lista_mascota.html', data)
        return HttpResponse(pdf, content_type='application/pdf')