from django.shortcuts import render
from . import models

def programm_lang_view(request):
    lang_value = models.ProgramLang.objects.all()
    return render(request, 'programm_lang.html', {'lang_key': lang_value})