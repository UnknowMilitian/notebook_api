from rest_framework import serializers
from notebook.models import User, Category, Media, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title", "order")


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ("id", "title", "file")


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    image = MediaSerializer(many=True, read_only=True)
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "category",
            "title",
            "image",
            "author",
            "created_at",
            "updated_at",
            "body",
        )
