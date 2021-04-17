from django.db import models

# Create your models here.

class Nasabah(models.Model):
    id_nasabah = models.CharField(max_length=16)
    nama = models.CharField(max_length=60)
    jenis_kelamin = models.CharField(max_length=20)
    alamat = models.TextField()
    usia = models.IntegerField()
    foto = models.ImageField(upload_to="",null=True)
    
    def __str__(self):
        return self.nama
