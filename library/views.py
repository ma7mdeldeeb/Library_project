from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .filters import BookFilter, AuthorFilter


@api_view(["GET"])
def list_book(request):
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    filtered_queryset = filterset_class(request.GET, queryset=queryset).qs
    paginator = PageNumberPagination()
    paginator.page_size = 10 
    paginated_queryset = paginator.paginate_queryset(filtered_queryset, request)

    serializer = BookSerializer(paginated_queryset, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(["GET"])
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)


@api_view(["GET"])
def list_author(request):
    queryset = Author.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = AuthorFilter
    filtered_queryset = filterset_class(request.GET, queryset=queryset).qs
    paginator = PageNumberPagination()
    paginator.page_size = 10 
    paginated_queryset = paginator.paginate_queryset(filtered_queryset, request)

    serializer = AuthorSerializer(paginated_queryset, many=True)
    return paginator.get_paginated_response(serializer.data)



@api_view(["GET"])
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)




@api_view(["POST"])
def order_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    user = request.user

    existing_order = Order.objects.filter(user=user, book=book)
    if existing_order.exists():
        return Response({'message': 'You have already ordered this book.'}, status=400)

    order = Order(user=user, book=book)
    order.save()

    serializer = OrderSerializer(order)
    return Response(serializer.data, status=201)



@api_view(["GET"])
def list_orders(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10  
    queryset = Order.objects.all()
    paginated_queryset = paginator.paginate_queryset(queryset, request)

    serializer = OrderSerializer(paginated_queryset, many=True)
    return paginator.get_paginated_response(serializer.data)