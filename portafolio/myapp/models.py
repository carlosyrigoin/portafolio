from django.db import models

class Portafolio(models.Model):
  foto = models.URLField(max_length=200)
  titulo = models.CharField(max_length=200)
  descripcion = models.TextField()
  tags = models.CharField(max_length=200)
  urlgithub = models.URLField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)