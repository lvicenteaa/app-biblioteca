from django.db import models


# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    sinopsis = models.TextField(null=True, verbose_name='Sinopsis')
    isbn = models.CharField(max_length=20, verbose_name='ISBN', null=True)
    editorial = models.CharField(max_length=100, verbose_name='Editorial', default='No tiene')
    anio = models.IntegerField(verbose_name='Año de publicación', null=True)

    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Sinopsis: " + self.sinopsis
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()