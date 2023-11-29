from django.shortcuts import render

def home(request):
    title = "Untels"
    elementos_lista = [
        "Análisis y Diseño de Sistemas",
        "Introducción a la Programación",
        "Algoritmos y Estructura de Datos",
        "Sistemas de Información",
        "Sistemas Operativos",
        "Arquitectura de Computadoras",
        "Desarrollo de apps moviles"
    ]
    return render(request, 'miapp/home.html', {'title': title, 'elementos_lista': elementos_lista})

def primos(request, a=1, b=100):
    a, b = int(a), int(b)
    if a > b:
        a, b = b, a

    # Calcula los números primos entre a y b
    numeros_primos = []
    for num in range(a, b + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                numeros_primos.append(num)

    context = {
        'title': 'Lista de Números Primos',
        'numeros_primos': numeros_primos,
    }
    return render(request, 'miapp/primos.html', context)

def inicio(request):
    cursos = [
        'Análisis y Diseño de Sistemas',
        'Introducción a la Programación',
        'Algoritmos y Estructura de Datos',
        'Sistemas de Información',
        'Sistemas Operativos',
        'Arquitectura de Computadoras',
        'Desarrollo de apps moviles',
    ]
    context = {
        'title': 'Cursos',
        'cursos': cursos,
    }
    return render(request, 'miapp/inicio.html', context)

def examen(request):
    informacion_examen = {
        'titulo': 'Información del Examen',
        'descripcion': 'Lista de integrantes',
    }
    return render(request, 'miapp/examen.html', informacion_examen)