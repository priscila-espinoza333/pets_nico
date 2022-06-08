from django.shortcuts import render


def productos_index(request):
    return render(request, 'productos.html')