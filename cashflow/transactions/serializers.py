from rest_framework import serializers

from . import models


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = "__all__"


class OperationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OperationType
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubCategory
        fields = "__all__"


class CashFlowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CashFlowRecord
        fields = "__all__"

    def validate(self, data):
        category = data.get("category", getattr(self.instance, "category", None))
        operation_type = data.get(
            "operation_type", getattr(self.instance, "operation_type", None)
        )
        subcategory = data.get(
            "subcategory", getattr(self.instance, "subcategory", None)
        )
        if category and operation_type and category.operation_type != operation_type:
            raise serializers.ValidationError(
                "Категория не принадлежит выбранному типу операции."
            )
        if subcategory and category and subcategory.category != category:
            raise serializers.ValidationError(
                "Подкатегория не принадлежит выбранной категории."
            )
        return data
