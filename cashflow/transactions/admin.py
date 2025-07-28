from django.contrib import admin

from . import models


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.OperationType)
class OperationTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "operation_type")
    list_filter = ("operation_type",)


@admin.register(models.SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category",)


@admin.register(models.CashFlowRecord)
class CashFlowRecordAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "status",
        "operation_type",
        "category",
        "subcategory",
        "price",
        "comment",
    )
    list_filter = ("status", "operation_type", "category", "subcategory", "created_at")
