from django.urls import path
from . import views

app_name = "notebook"

urlpatterns = [
    path("users", views.UserAPIView.as_view(), name="users"),
    path(
        "user-detail/<int:pk>", views.UserDetailAPIView.as_view(), name="users_detail"
    ),
    path("categories", views.CategoryListAPIView.as_view(), name="category_list"),
    path(
        "category/<int:pk>",
        views.CategoryRetriveAPIView.as_view(),
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
    path("post-detail/<int:pk>", views.PostRetriveAPIView.as_view(), name="post_detail"),
    path(
        "recently-posts", views.RecentlyPostListAPIView.as_view(), name="recently_list"
    ),
    path("popular-posts", views.PopularPostsAPIView.as_view(), name="popular_posts"),
    path("todays-posts", views.TodaysPostsAPIView.as_view(), name="todays_posts"),
    path(
        "featured-this-month-posts",
        views.FeaturedThisMonthAPIVIew.as_view(),
        name="featured_this_month_posts",
    ),
    path(
        "top-authors", views.TopAuthorsAPIView.as_view(), name="top_authors"
    ),  # Исправленный путь
]
