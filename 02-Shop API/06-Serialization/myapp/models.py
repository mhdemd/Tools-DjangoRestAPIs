from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title


class Product(models.Model):
    web_id = models.CharField(
        max_length=50,
        verbose_name=_("Product Website ID"),
        help_text=_("Required, unique"),
        unique=False,
        null=True,
        blank=True,
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name=_("Product Safe URL"),
        help_text=_("Required, letters, numbers, underscores, or hyphens"),
        unique=False,
        null=False,
        blank=True,
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("Product Name"),
        help_text=_("Required, max 255 characters"),
        unique=False,
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name=_("Product Description"),
        help_text=_("Required"),
        unique=False,
        null=False,
        blank=False,
    )
    is_active = models.BooleanField(
        verbose_name=_("Product Visibility"),
        help_text=_("True = Product Visible"),
        default=True,
        unique=False,
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Date Product Created"),
        help_text=_("Format: Y-m-d H:M:S"),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Date Product Last Updated"),
        help_text=_("Format: Y-m-d H:M:S"),
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT) 
    
    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created_at"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
