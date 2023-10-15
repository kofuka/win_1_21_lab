from django.shortcuts import render
from . import models

def book_view(request):
    lang_value = models.Book.objects.all()
    return render(request, 'book.html', {'lang_key': lang_value})