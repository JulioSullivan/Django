from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    context = models.TextField(verbose_name="Contexto")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación") # Cuando se crea
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición") # Cada vez que se actualiza

    class Meta:
        verbose_name = 'servico'
        verbose_name_plural = 'servicios'
        ordering = ["-created"] # Guión para que se ordene dioferente con la fecha, del más nuevo a l más viejo

    def __str__(self):
        return self.title