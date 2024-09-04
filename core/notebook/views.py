# Main imports
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.db.models import Count
from rest_framework import status

# Tools
from rest_framework.pagination import LimitOffsetPagination
from django.utils.timezone import now

# Models
from notebook.models import User, Category, Media, Post, PostView

# Serializers
from notebook.serializers import (
    CategorySerializer,
    CategoryCountSerializer,
    CategoryCountMethodSerializer,
    MediaSerializer,
    AuthorSerializer,
    PostSerializer,
)


# Standart view Classes
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
    pagination_class = LimitOffsetPagination

    def view_count(self):
        return self.views.count()


class PostDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(
                {"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND
            )


class RecentlyPostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by("-id")
    pagination_class = LimitOffsetPagination


class FeaturedThisMonthAPIVIew(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        current_data = now()
        return Post.objects.filter(
            created_at__year=current_data.year, created_at__month=current_data.month
        ).order_by("-created_at")

    pagination_class = LimitOffsetPagination


class TopAuthorsAPIView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = User.objects.annotate(count_post=Count("posts")).order_by("-count_post")[
        :3
    ]
