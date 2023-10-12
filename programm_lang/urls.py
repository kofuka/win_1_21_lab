from django.urls import path
from . import views

urlpatterns = [
    path('programm_lang/', views.programm_lang_view),
]