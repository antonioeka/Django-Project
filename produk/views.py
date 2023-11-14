from django.shortcuts import render, redirect
from produk.forms import FormBarang, FormUser_Management
from produk.models import Barang, User_Management
from django.contrib import messages
# Create your views here.

def update_barang(request, id_barang):
    barangs = Barang.objects.get(id = id_barang)
    if request.POST:
        form=FormBarang(request.POST, instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diubah")
            return redirect('update_barang', id_barang = id_barang)
    else:
        form = FormBarang(instance=barangs)
        konteks = {
            'form' : form,
            'barangs' : barangs
        }
    return render(request, 'update_barang.html', konteks)

def hapus_barang(request, id_barang):
    barangs = Barang.objects.filter(id = id_barang)
    barangs.delete()
    messages.success(request, "Data Berhasil Dihapus")
    return redirect ('/tampil_brg.html')    

def tambah_barang(request):
    if request.POST:
        form = FormBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            form = FormBarang()
            konteks = {
                'form' : form,
            }
            return render(request, 'tambah_barang.html', konteks)
    else:
        form = FormBarang()
        konteks = {
            'form' : form,
        }
        return render(request, 'tambah_barang.html', konteks)
def Barang_View(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs,
    }

    return render((request), 'tampil_brg.html', konteks)

def update_user(request, username):
    user_managements = User_Management.objects.get(id = username)
    if request.POST:
        form=FormUser_Management(request.POST, instance=user_managements)
        if form.is_valid():
            form.save()
            messages.success(request, "Data User Berhasil Diubah")
            return redirect('update_user', username = username)
    else:
        form = FormUser_Management(instance=user_managements)
        konteks = {
            'form' : form,
            'user_managements' : user_managements
        }
    return render(request, 'update_user.html', konteks)

def hapus_user(request, username):
    user_managements = User_Management.objects.filter(id = username)
    user_managements.delete()
    messages.success(request, "User Berhasil Dihapus")
    return redirect ('/user_management.html')

def tambah_user(request):
    if request.POST:
        form = FormUser_Management(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Berhasil Ditambahkan")
            form = FormUser_Management()
            konteks = {
                'form' : form,
            }
            return render(request, 'tambah_user.html', konteks)
    else:
        form = FormUser_Management()
        konteks = {
            'form' : form,
        }
        return render(request, 'tambah_user.html', konteks)

def user_management(request):
    user_managements=User_Management.objects.all()

    konteks={
        'user_managements':user_managements,
    }

    return render((request), 'user_management.html', konteks)