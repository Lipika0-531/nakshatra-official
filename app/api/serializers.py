from rest_framework.serializers import ModelSerializer
from ..models import Categories, Products, Reviews
from rest_framework import serializers

class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields ='__all__'

        
class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = ('title', 'price', 'author', 'publised_on', 'avg_ratings', 'rating_count','category')



class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('rating', 'body')
