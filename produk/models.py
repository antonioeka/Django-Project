from django.db import models

# Create your models here.
class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

def __str__(self):
    return self.nama

class Barang(models.Model):
    kodebrg=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank=True)
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)

class Status(models.Model):
    nama = models.CharField(max_length=50)
    ket=models.TextField()
    
def __str__(self):
    return self.nama

class User_Management(models.Model):
    username =  models.CharField(max_length=20)
    nama = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=8)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)


# def __str__(self):
#     return self.nama

