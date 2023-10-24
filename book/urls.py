from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_view),
    path('book_detail/<int:id>/', views.book_detail_view),
    path('add-cooment/', views.createBookView),
    path('create_post_book/', views.createBookPostView),
    path('book_list/', views.book_delete_view),
    path('book_list/<int:id>/delete/', views.book_drop_view),
]
