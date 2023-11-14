from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from produk.views import *
def index(request):
    judul = "Home"
    konteks = {
        'title' : judul
    }
    return render(request,'index.html', konteks)

def about(request):
    judul = "About Me"
    konteks = {
        'title' : judul
    }
    return render(request, 'about-me.html', konteks)

def portofolio(request):
    judul = "Portfolio"
    konteks = {
        'title' : judul
    }
    return render(request, 'portfolio.html', konteks)

def contact(request):
    judul = "Contact"
    konteks = {
        'title' : judul
    }
    return render(request, 'contact.html', konteks)
  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index.html', index),
    path('about-me.html', about),
    path('portfolio.html', portofolio),
    path('contact.html', contact),
    path('tambah_barang.html', tambah_barang),
    path('tampil_brg.html', Barang_View),
    path('update_barang.html/<int:id_barang>', update_barang, name = 'update_barang'),
    path('hapus/<int:id_barang>', hapus_barang, name = 'hapus_barang'),
    path('user_management.html', user_management),
    path('tambah_user.html', tambah_user),
    path('update_user.html/<int:username>', update_user, name = 'update_user'),
    path('hapus/<int:username>', hapus_user, name = 'hapus_user'),
]

