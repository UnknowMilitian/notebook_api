from django.shortcuts import render
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, GenericAPIView

# Models
from notebook.models import User, Category, Media, Post

# Serializers
from notebook.serializers import (
    CategorySerializer,
    CategoryCountSerializer,
    CategoryCountMethodSerializer,
    MediaSerializer,
    AuthorSerializer,
    PostSerializer,
)


# Create your views here.
class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetailAPIView(APIView):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)

        return Response(serializer.data)


class CategoryCountAPIView(APIView):
    def get(self, request):
        categories = (
            Category.objects.annotate(count=Count("posts")).order_by("-order").all()
        )
        serializer = CategoryCountSerializer(categories, many=True)
        return Response(serializer.data)


class CategoryCountMethodAPIView(APIView):
    def get(self, request):
        categories = Category.objects.prefetch_related("posts").all()
        serializer = CategoryCountMethodAPIView(categories, many=True)
        return Response(serializer.data)


class MediaListAPIView(ListAPIView):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()


class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class TopAuthorsAPIView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = User.objects.annotate(count_post=Count("posts")).order_by("-count_post")[
        :3
    ]
