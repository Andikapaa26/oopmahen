from django.db import models

# Create your models here.
class Kota(models.Model):
    nama = models.CharField(max_length=100)
    pejabat = models.CharField(max_length=100)
    wisata = models.CharField(max_length=100,null=True)

    def __str__(self) -> str:
        return self.nama

class Peta(models.Model):
    nama = models.CharField(max_length=100)
    bentang_alam = models.CharField(max_length=100)
    x = models.CharField(max_length=100)
    y = models.CharField(max_length=100)

    def __str__(self):
        return self.nama