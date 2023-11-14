from django.contrib import admin

# Register your models here.
from .models import Barang, Jenis, User_Management, Status

class kolomBarang(admin.ModelAdmin):
    list_display = ['kodebrg', 'nama', 'stok', 'harga', 'link_gbr', "jenis_id"]
    search_fields = ['kodebrg', 'nama']
    list_filter = ('jenis_id',)
    list_per_page = 3

class kolomUser_Management(admin.ModelAdmin):
    list_display = ['username', 'nama', 'email', 'password', 'status']
    search_fields = ['username', 'nama']

admin.site.register(User_Management, kolomUser_Management)
admin.site.register(Status)
admin.site.register(Barang, kolomBarang)
admin.site.register(Jenis)