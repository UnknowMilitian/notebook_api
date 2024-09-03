from django.urls import path
from . import views  # Импортируем файл views, где определен TopAuthorsAPIView

app_name = "notebook"

urlpatterns = [
    path("categories", views.CategoryListAPIView.as_view(), name="category_list"),
    path(
        "category/<int:pk>",
        views.CategoryDetailAPIView.as_view(),
        name="category_detail",
    ),
    path(
        "category-count/", views.CategoryCountAPIView.as_view(), name="category_count"
    ),
    path(
        "category-count-method/",
        views.CategoryCountMethodAPIView.as_view(),
        name="category_count_method",
    ),
    path("medias", views.MediaListAPIView.as_view(), name="media_list"),
    path("posts", views.PostListAPIView.as_view(), name="post_list"),
    path(
        "top-authors", views.TopAuthorsAPIView.as_view(), name="top_authors"
    ),  # Исправленный путь
]
