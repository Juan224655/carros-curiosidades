from django.urls import path

from . import views

urlpatterns = [
    path("", views.MarcaListView.as_view(), name="marca_list"),
    path("marcas/nova/", views.MarcaCreateView.as_view(), name="marca_create"),
    path("marcas/<int:pk>/", views.MarcaDetailView.as_view(), name="marca_detail"),
    path("marcas/<int:pk>/editar/", views.MarcaUpdateView.as_view(), name="marca_update"),
    path("marcas/<int:pk>/excluir/", views.MarcaDeleteView.as_view(), name="marca_delete"),
    path("marcas/<int:marca_pk>/carros/novo/", views.CarroCreateView.as_view(), name="carro_create"),
    path("marcas/<int:marca_pk>/curiosidades/nova/", views.CuriosidadeCreateView.as_view(), name="curiosidade_create"),
    path("marcas/<int:marca_pk>/comentar/", views.comentar, name="comentar"),
]
