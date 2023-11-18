from rest_framework import serializers
from .models import *



class ReviewSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

# serializers.py
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'




class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'



