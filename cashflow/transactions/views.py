from rest_framework import viewsets

from . import models, serializers


class StatusViewSet(viewsets.ModelViewSet):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer


class OperationTypeViewSet(viewsets.ModelViewSet):
    queryset = models.OperationType.objects.all()
    serializer_class = serializers.OperationTypeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.SubCategory.objects.all()
    serializer_class = serializers.SubCategorySerializer


class CashFlowRecordViewSet(viewsets.ModelViewSet):
    queryset = models.CashFlowRecord.objects.all()
    serializer_class = serializers.CashFlowRecordSerializer
