from django.contrib import admin
from .models import Category
from .models import Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    perpulated_fields = {"slug" : ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
            "name", 
            "slug",
            "price",
            "available",
            "created",
            "updated"
            ]

    list_filters = ["available", "created", "updated"]
    list_editable = ["price", "available"]
    perpulated_fields = {"slug" : ("name",)}
