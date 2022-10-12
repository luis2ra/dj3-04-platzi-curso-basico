from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from polls.models import Question


def index(request):
    print("Las vistas siempre reciben un parametro tipo <request>", type(request))
    print("El request tiene un parametro <headers>: ", request.headers)
    print("El request tiene un parametro <POST>: ", request.POST)

    latest_question_list = Question.objects.all()

    return render(
        request,
        "polls/index.html",
        {
            "latest_question_list": latest_question_list
        }
    )


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(
        request,
        "polls/detail.html",
        {
            "question": question
        }
    )


def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta nro.: {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta nro.: {question_id}")
