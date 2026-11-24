from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CarroForm, ComentarioForm, CuriosidadeForm, MarcaForm
from .models import Marca


class MarcaListView(ListView):
    model = Marca
    template_name = "curiosidades/marca_list.html"
    context_object_name = "marcas"

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(Q(nome__icontains=q) | Q(pais__icontains=q))
        return qs


class MarcaDetailView(DetailView):
    model = Marca
    template_name = "curiosidades/marca_detail.html"
    context_object_name = "marca"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["comentario_form"] = ComentarioForm()
        return ctx


class MarcaCreateView(LoginRequiredMixin, CreateView):
    form_class = MarcaForm
    template_name = "curiosidades/form.html"
    extra_context = {"titulo": "Nova marca"}


class MarcaUpdateView(LoginRequiredMixin, UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = "curiosidades/form.html"
    extra_context = {"titulo": "Editar marca"}


class MarcaDeleteView(LoginRequiredMixin, DeleteView):
    model = Marca
    template_name = "curiosidades/marca_confirm_delete.html"
    success_url = reverse_lazy("marca_list")


class CarroCreateView(LoginRequiredMixin, CreateView):
    form_class = CarroForm
    template_name = "curiosidades/form.html"
    extra_context = {"titulo": "Novo carro"}

    def form_valid(self, form):
        form.instance.marca = get_object_or_404(Marca, pk=self.kwargs["marca_pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("marca_detail", args=[self.kwargs["marca_pk"]])


class CuriosidadeCreateView(LoginRequiredMixin, CreateView):
    form_class = CuriosidadeForm
    template_name = "curiosidades/form.html"
    extra_context = {"titulo": "Nova curiosidade"}

    def form_valid(self, form):
        form.instance.marca = get_object_or_404(Marca, pk=self.kwargs["marca_pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("marca_detail", args=[self.kwargs["marca_pk"]])


@login_required
def comentar(request, marca_pk):
    marca = get_object_or_404(Marca, pk=marca_pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.marca = marca
            comentario.autor = request.user
            comentario.save()
    return redirect("marca_detail", pk=marca.pk)


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("marca_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
