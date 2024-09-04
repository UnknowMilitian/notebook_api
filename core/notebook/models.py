from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


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