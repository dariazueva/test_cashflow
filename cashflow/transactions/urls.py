from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("statuses", views.StatusViewSet)
router.register("operation-types", views.OperationTypeViewSet)
router.register("categories", views.CategoryViewSet)
router.register("subcategories", views.SubCategoryViewSet)
router.register("cashflow-records", views.CashFlowRecordViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
