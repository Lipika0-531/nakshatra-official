from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer
from ..models import Categories, Products, Reviews, User
from rest_framework import fields, serializers



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields='__all__'

class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields ='__all__'



class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('user', 'product','rating','body')

    def to_representation(self, instance):
        response= super().to_representation(instance)
        response['user'] =  UserSerializer(instance.user).data
        response['product'] =ProductsSerializer(instance.product).data
        return response


class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = ('title', 'price', 'author', 'publised_on', 'avg_ratings', 'rating_count','category', 'user','description')


# class ContentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Content
#         fields = ('title', 'body', 'topic')

#     def to_representation(self, instance):
#         response = super().to_representation(instance)
#         response['topic'] = TopicSerializer(instance.topic).data
#         return response