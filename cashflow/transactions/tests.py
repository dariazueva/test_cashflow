from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

from .models import CashFlowRecord, Category, OperationType, Status, SubCategory


class CashFlowModelTests(TestCase):
    def setUp(self):
        self.status = Status.objects.create(name="Бизнес")
        self.op_type = OperationType.objects.create(name="Пополнение")
        self.op_type_other = OperationType.objects.create(name="Списание")
        self.category = Category.objects.create(
            name="Инфраструктура", operation_type=self.op_type
        )
        self.subcategory = SubCategory.objects.create(
            name="VPS", category=self.category
        )

    def test_valid_cashflow_record(self):
        record = CashFlowRecord(
            status=self.status,
            operation_type=self.op_type,
            category=self.category,
            subcategory=self.subcategory,
            price=1000,
        )
        record.clean()

    def test_invalid_category_operation_type(self):
        record = CashFlowRecord(
            status=self.status,
            operation_type=self.op_type_other,
            category=self.category,
            subcategory=self.subcategory,
            price=1000,
        )
        with self.assertRaises(ValidationError):
            record.clean()

    def test_invalid_subcategory_category(self):
        other_category = Category.objects.create(
            name="Маркетинг", operation_type=self.op_type
        )
        record = CashFlowRecord(
            status=self.status,
            operation_type=self.op_type,
            category=other_category,
            subcategory=self.subcategory,
            price=1000,
        )
        with self.assertRaises(ValidationError):
            record.clean()


class CashFlowAPITests(APITestCase):
    def setUp(self):
        self.status = Status.objects.create(name="Бизнес")
        self.op_type = OperationType.objects.create(name="Пополнение")
        self.category = Category.objects.create(
            name="Инфраструктура", operation_type=self.op_type
        )
        self.subcategory = SubCategory.objects.create(
            name="VPS", category=self.category
        )

    def test_create_cashflow_record(self):
        url = reverse("cashflowrecord-list")
        payload = {
            "status": self.status.id,
            "operation_type": self.op_type.id,
            "category": self.category.id,
            "subcategory": self.subcategory.id,
            "price": "1000.00",
            "comment": "Тестовая операция",
        }
        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(CashFlowRecord.objects.count(), 1)

    def test_list_cashflow_records(self):
        CashFlowRecord.objects.create(
            status=self.status,
            operation_type=self.op_type,
            category=self.category,
            subcategory=self.subcategory,
            price=500,
        )
        url = reverse("cashflowrecord-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_update_cashflow_record(self):
        record = CashFlowRecord.objects.create(
            status=self.status,
            operation_type=self.op_type,
            category=self.category,
            subcategory=self.subcategory,
            price=500,
        )
        url = reverse("cashflowrecord-detail", args=[record.id])
        response = self.client.patch(url, {"price": "1500.00"}, format="json")
        self.assertEqual(response.status_code, 200)
        record.refresh_from_db()
        self.assertEqual(str(record.price), "1500.00")

    def test_delete_cashflow_record(self):
        record = CashFlowRecord.objects.create(
            status=self.status,
            operation_type=self.op_type,
            category=self.category,
            subcategory=self.subcategory,
            price=500,
        )
        url = reverse("cashflowrecord-detail", args=[record.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(CashFlowRecord.objects.count(), 0)
