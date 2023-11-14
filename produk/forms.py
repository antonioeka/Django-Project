from django.forms import ModelForm
from django import forms
from produk.models import Barang, User_Management

class FormBarang(ModelForm):
    class Meta :
        model = Barang
        fields='__all__'

    widgets = {
        'kodebrg' : forms.TextInput({
            'class' : 'form-control'
        }),
        'nama' : forms.TextInput({
            'class' : 'form-control'
        }),
        'stok' : forms.NumberInput({
            'class' : 'form-control'
        }),
        'harga' : forms.NumberInput({
            'class' : 'form-control'
        }),
        'link_gbr' : forms.TextInput({
            'class' : 'form-control'
        }),
        'jenis_id' : forms.Select({
            'class' : 'form-control'
        }),
    }

class FormUser_Management(ModelForm):
    class Meta :
        model = User_Management
        fields='__all__'

    widgets = {
        'username' : forms.TextInput({
            'class' : 'form-control'
        }),
        'nama' : forms.TextInput({
            'class' : 'form-control'
        }),
        'email' : forms.TextInput({
            'class' : 'form-control'
        }),
        'password' : forms.TextInput({
            'class' : 'form-control'
        }),
        'status' : forms.Select({
            'class' : 'form-control'
        }),
    }