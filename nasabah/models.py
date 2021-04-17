from django.db import models
from django.utils.timezone import now

# Create your models here.

class Nasabah(models.Model):
    jenkel = [
        ('Pria', 'Pria'),
        ('Wanita', 'Wanita'),
    ]
    id_nasabah = models.CharField(max_length=16)
    nama = models.CharField(max_length=60)
    jenis_kelamin = models.CharField(max_length=6,choices=jenkel)
    alamat = models.TextField()
    usia = models.IntegerField()
    foto = models.ImageField(upload_to="",null=True)
    date_register = models.DateTimeField(default=now, blank=True)
    isAuthenticate = models.BooleanField(default=False)
    dateAuthenticate = models.DateTimeField(default=now, blank=True)
    
    def __str__(self):
        return self.nama
