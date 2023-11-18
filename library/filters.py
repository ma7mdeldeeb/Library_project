import django_filters
from .models import Book, Author

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')
    author__name = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['title', 'author__name', 'min_price', 'max_price']


# filters.py
class AuthorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    books__title = django_filters.CharFilter(field_name='books__title', lookup_expr='icontains')

    class Meta:
        model = Author
        fields = ['name', 'books__title']

