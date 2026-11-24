from django.contrib import admin

from .models import Carro, Comentario, Curiosidade, Marca



class CarroInline(admin.TabularInline):
    model = Carro
    extra = 1


class CuriosidadeInline(admin.TabularInline):
    model = Curiosidade
    extra = 1


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ("nome", "pais", "ano_fundacao")
    search_fields = ("nome", "pais")
    inlines = [CarroInline, CuriosidadeInline]


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ("modelo", "marca", "ano")
    list_filter = ("marca",)


@admin.register(Curiosidade)
class CuriosidadeAdmin(admin.ModelAdmin):
    list_display = ("titulo", "marca")
    list_filter = ("marca",)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("autor", "marca", "criado_em")
    list_filter = ("marca",)
