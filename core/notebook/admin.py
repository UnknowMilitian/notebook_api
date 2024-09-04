from django.contrib import admin
from notebook.models import Category, Media, Post, PostView


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(PostView)
class PostViewAdmin(admin.ModelAdmin):
    pass
