from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = models.TextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación") # Cuando se crea
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición") # Cada vez que se actualiza

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"

    def __str__(self):
        return self.title