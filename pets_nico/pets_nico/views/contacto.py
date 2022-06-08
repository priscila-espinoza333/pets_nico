from django.shortcuts import render

def contacto_index(request):
    print('contacto_index')
    return render(request, 'contacto.html')

def formulario_contacto(request):
    print('formulario_contacto')

    if request.method == 'GET':
        print('invocación por método GET')
        run = request.GET.get('run')
        print('run {0}'.format(run))

    elif request.method == 'POST':
        print('invocación por método POST')
        run = request.POST.get('run')
        print('run {0}'.format(run))

    return render(request, 'contacto.html')