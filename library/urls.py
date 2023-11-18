from django.urls import path
from .views import *

urlpatterns = [
    path('list_books/',list_book, name='book_list'),
    path('book_detail/<int:pk>/', book_detail, name='book_detail'),
    path('author_detail/<int:pk>/', author_detail, name='auther_detail'),
    path('author_list/', list_author, name='list_author'),    
    path('orders/', list_orders, name='list_orders'),
    path('orders/<int:pk>/', order_book, name='order_detail'),
]
