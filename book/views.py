from django.shortcuts import render,  get_object_or_404
from . import models

def book_view(request):
    lang_value = models.Book.objects.all()
    return render(request, 'book.html', {'lang_key': lang_value})

def book_detail_view(request, id):
    lang_id = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html', {'lang_key': lang_id})