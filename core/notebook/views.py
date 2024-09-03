from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, GenericAPIView

# Models
from notebook.models import Category, Media, Post

# Serializers
from notebook.serializers import CategorySerializer, MediaSerializer, PostSerializer


# Create your views here.
class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class MediaListAPIView(ListAPIView):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()


class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
