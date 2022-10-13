from django.contrib import admin
from polls.models import Question, Choice


admin.site.register([Question, Choice])  # se define una lista de los modelos a verse en el Admin de Django
