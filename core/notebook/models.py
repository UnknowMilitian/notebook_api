from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(_("Fullname"), max_length=255)
    info = models.CharField(_("Info"), max_length=255)
    facebook = models.CharField(_("Facebook"), max_length=255, null=True, blank=True)
    twitter = models.CharField(_("Twitter"), max_length=255, null=True, blank=True)
    instagram = models.CharField(_("Instagram"), max_length=255, null=True, blank=True)
    avatar = models.FileField(
        _("Avatar"), upload_to="profile_avatar", null=True, blank=True
    )
    description = models.TextField(_("Description"), null=True, blank=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    order = models.IntegerField(_("Order"), default=0)

    objects = models.Manager()

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


class Media(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    file = models.FileField(_("Image"), upload_to="posts_images")

    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Medias"

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name=_("Category"),
        related_name="posts",
    )
    title = models.CharField(_("Title"), max_length=255)
    image = models.ManyToManyField(to=Media, related_name="post_image")
    author = models.ForeignKey(
        User, related_name="posts", on_delete=models.CASCADE, verbose_name=_("Author")
    )
    created_at = models.DateField(_("Date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    body = models.TextField(_("Text"))

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title


class PostView(models.Model):
    post = models.ForeignKey(Post, related_name="views", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    view_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        return f"{self.user} - {self.post}"
