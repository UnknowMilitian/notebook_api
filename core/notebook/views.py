# Main imports
from rest_framework.generics import ListAPIView, GenericAPIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.timezone import now
from rest_framework import generics
from django.shortcuts import render
from django.db.models import Count
from rest_framework import status


# Tools
from rest_framework.pagination import LimitOffsetPagination
from django.utils.timezone import now

# Models
from notebook.models import Profile, Category, Media, Post

# Serializers
from notebook.serializers import (
    ProfileSerializer,
    ProfileDetailSerializer,
    UserSerializer,
    UserDetailSerializer,
    CategorySerializer,
    CategoryCountSerializer,
    CategoryCountMethodSerializer,
    MediaSerializer,
    AuthorSerializer,
    PostSerializer,
)

User = get_user_model()


# Standart view Classes
class UserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserDetailSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )


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
            if request.user.is_authenticated:
                PostView.objects.get_or_create(post=post, user=request.user)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response(
                {"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND
            )


class RecentlyPostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by("-id")
    pagination_class = LimitOffsetPagination


class PopularPostsAPIView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.annotate(view_count=Count("views")).order_by("-view_count")[
            :3
        ]


class TodaysPostsAPIView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        today = now().date()
        return Post.objects.filter(created_at=today).order_by("-created_at")


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


# For creating CRUD for models
class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination


class CategoryRetriveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MediaListAPIView(generics.ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination


class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination


class PostRetriveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = CategorySerializer
