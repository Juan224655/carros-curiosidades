from django.conf import settings
from django.db import models
from django.urls import reverse


class Marca(models.Model):
    nome = models.CharField(max_length=80, unique=True)
    pais = models.CharField("país de origem", max_length=60)
    ano_fundacao = models.PositiveIntegerField("ano de fundação")
    descricao = models.TextField("descrição")
    foto = models.ImageField("foto / logo", upload_to="marcas/", blank=True, null=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("marca_detail", args=[self.pk])


class Carro(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name="carros")
    modelo = models.CharField(max_length=80)
    ano = models.PositiveIntegerField()
    descricao = models.TextField("descrição", blank=True)
    foto = models.ImageField(upload_to="carros/", blank=True, null=True)

    class Meta:
        ordering = ["modelo"]

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"


class Curiosidade(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name="curiosidades")
    titulo = models.CharField("título", max_length=120)
    texto = models.TextField()

    class Meta:
        verbose_name_plural = "curiosidades"

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name="comentarios")
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField("comentário")
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em"]

    def __str__(self):
        return f"{self.autor} em {self.marca}"
