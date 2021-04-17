from rest_framework import serializers
from django.utils.timezone import now

from .models import Nasabah

class NasabahSerializer(serializers.Serializer):
    id_nasabah = serializers.CharField(max_length=16)
    nama = serializers.CharField(max_length=60)
    jenis_kelamin = serializers.CharField(max_length=6)
    alamat = serializers.CharField()
    usia = serializers.IntegerField()
    foto = serializers.CharField(max_length=40)
    date_register = serializers.DateTimeField(default=now)
    isAuthenticate = serializers.BooleanField(default=False)
    dateAuthenticate = serializers.DateTimeField(default=now)

    def create(self, validated_data):
        return Nasabah.objects.create(validated_data)

    
    def update(self, instance, validated_data):
        instance.id_nasabah = validated_data.get('id_nasabah', instance.id_nasabah)
        instance.nama = validated_data.get('nama', instance.nama)
        instance.jenis_kelamin = validated_data.get('jenis_kelamin', instance.jenis_kelamin)
        instance.alamat = validated_data.get('alamat', instance.alamat)
        instance.usia = validated_data.get('usia', instance.usia)
        instance.foto = validated_data.get('foto', instance.foto)
        instance.date_register = validated_data.get('date_register', instance.date_register)
        instance.isAuthenticate = validated_data.get('isAuthenticate', instance.isAuthenticate)
        instance.dateAuthenticate = validated_data.get('dateAuthenticate', instance.dateAuthenticate)
        instance.save()
        return instance