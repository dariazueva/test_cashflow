from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Status(models.Model):
    """Справочник статусов."""

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return self.name


class OperationType(models.Model):
    """Справочник типов операций."""

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Тип операции"
        verbose_name_plural = "Типы операций"

    def __str__(self):
        return self.name


class Category(models.Model):
    """Категории, привязанные к типу операций."""

    name = models.CharField(max_length=100)
    operation_type = models.ForeignKey(
        OperationType,
        on_delete=models.CASCADE,
        related_name="categories",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        unique_together = ("name", "operation_type")

    def __str__(self):
        return f"{self.name} ({self.operation_type})"


class SubCategory(models.Model):
    """Подкатегории, привязанные к категории."""

    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories",
    )

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        unique_together = ("name", "category")

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class CashFlowRecord(models.Model):
    """Основная модель учета ддс."""

    created_at = models.DateField(default=timezone.localdate)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    operation_type = models.ForeignKey(
        OperationType,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Запись ДДС"
        verbose_name_plural = "Записи ДДС"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.created_at} | {self.operation_type} | {self.price} руб."

    def clean(self):
        if self.category.operation_type != self.operation_type:
            raise ValidationError(
                "Категория не соответствует выбранному типу операции."
            )
        if self.subcategory.category != self.category:
            raise ValidationError("Подкатегория не соответствует выбранной категории.")
