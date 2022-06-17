from re import template
from django.urls import path
from .views import listar_rechazadas, ver_rechazada,ver_aprobada,listar_aprobadas,rechazar_solicitud,aceptar_solicitud, ver_solicitud,eliminar_solicitudes,listar_solicitudes,eliminar_mascota_desaparecida,listar_mascotas_desaparecidas,home, contacto, agregar_mascota, listar_mascotas, modificar_mascota, eliminar_mascota, nosotros, registro, agregar_mascota_desaparecida, mascotasDesaparecidas, formulario_adopcion, ListaMascotasListView, ListMascotasPdf
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('agregar-mascota/', agregar_mascota, name="agregar_mascota"),
    path('listar-mascotas/', listar_mascotas, name="listar_mascotas"),
    path('modificar-mascota/<id>/', modificar_mascota, name="modificar_mascota"),
    path('eliminar-mascota/<id>/', eliminar_mascota, name="eliminar_mascota"),
    path('registro/', registro, name="registro"),
    path('quienes-somos/', nosotros, name="nosotros"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="registration/login.html")),
    path('agregar_mascota_desaparecida/', agregar_mascota_desaparecida, name="agregar_mascota_desaparecida"),
    path('listar_mascota_desaparecida/', listar_mascotas_desaparecidas, name="listar_mascotas_desaparecidas"),
    path('eliminar_desaparecida/<id>/', eliminar_mascota_desaparecida, name="eliminar_mascota_desaparecida"),
    path('mascotas_desaparecidas/', mascotasDesaparecidas, name="mascotas_desaparecidas"),
    path('solicitud_adopcion/', formulario_adopcion, name="solicitud_adopcion"),
    path('listado_solicitudes/', listar_solicitudes, name="listar_solicitudes"),
    path('listado_aprobadas/', listar_aprobadas, name="listar_aprobadas"),
    path('listado_rechazadas/', listar_rechazadas, name="listar_rechazadas"),
    path('eliminar_solicitud/<id>/', eliminar_solicitudes, name="eliminar_solicitud"),
    path('ver_rechazada/<id>/', ver_rechazada, name="ver_rechazada"),
    path('ver_solicitud/<id>/', ver_solicitud, name="ver_solicitud"),
    path('ver_aprobada/<id>/', ver_aprobada, name="ver_aprobada"),
    path('aceptar_solicitud/<id>/', aceptar_solicitud, name="aceptar_solicitud"),
    path('rechazar_solicitud/<id>/', rechazar_solicitud, name="rechazar_solicitud"),
    path('lista_mascota/', ListaMascotasListView.as_view(),name="lista_mascota"),
    path('list_mascota_pdf/', ListMascotasPdf.as_view(),name="mascotas_all"),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="registration/recuperar_contraseña.html"
    ), name="reset_password"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name="registration/recuperar_mensaje.html"
    ), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="registration/recuperar_form.html"
    ), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name="registration/recuperar_done.html"
    ), name="password_reset_complete"),
    
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name = "registration/cambiar_pw.html"
    ), name="password_change"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name = "registration/cambiar_pw_done.html"
    ), name="password_change"),

]