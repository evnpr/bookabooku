from django.db import models

# Create your models here.

class Book(models.Model):
  id = models.AutoField(primary_key=True)
  judul = models.CharField(max_length=500)
  seri = models.CharField(max_length=500)
  pengarang = models.CharField(max_length=500)
  tipe = models.CharField(max_length=500)
  jumlah = models.CharField(max_length=500)
  harga_modal = models.CharField(max_length=500)
  harga_display = models.CharField(max_length=500)
  tambahan = models.CharField(max_length=500)
  langka = models.BooleanField()

