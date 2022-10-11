from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print("Las vistas siempre reciben un parametro tipo <request>", type(request))
    print("El request tiene un parametro <headers>: ", request.headers)
    # print("El request tiene un parametro <data>: ", request.data)
    return HttpResponse("Estas en la pagina principal de Premios Platzi!")


def detail(request, question_id):
    # print("El request tiene un parametro <data>: ", request.data)
    return HttpResponse(f"Estas viendo la pregunta nro.: {question_id}")


def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta nro.: {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta nro.: {question_id}")
