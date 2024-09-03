from django.urls import path
from . import views

app_name = "notebook"

urlpatterns = [
    path("categories", views.CategoryListAPIView.as_view(), name="category_list"),
    path("medias", views.MediaListAPIView.as_view(), name="media_list"),
    path("posts", views.PostListAPIView.as_view(), name="post_list"),
]
