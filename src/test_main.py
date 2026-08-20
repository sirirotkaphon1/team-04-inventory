import unittest
from src.main import InventoryManager, Product

class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.inv = InventoryManager()
        self.p1 = Product(id="P01", name="สายไฟ 2.5 sq.mm", category="งานไฟฟ้า", price=250.0, stock=20, threshold=15)
        self.p2 = Product(id="P02", name="ท่อ PVC 1 นิ้ว", category="งานประปา", price=300.0, stock=10, threshold=5)
        self.inv.add_product(self.p1)
        self.inv.add_product(self.p2)

    def test_release_stock_success(self):
        """ทดสอบการจ่ายสินค้าปกติ"""
        result = self.inv.release_stock("P01", 8)
        self.assertTrue(result)
        self.assertEqual(self.p1.stock, 12)

    def test_release_stock_insufficient(self):
        """ทดสอบจ่ายสินค้าเมื่อสต็อกไม่พอ"""
        result = self.inv.release_stock("P02", 15)
        self.assertFalse(result)
        self.assertEqual(self.p2.stock, 10)

    def test_release_stock_invalid_quantity(self):
        """ทดสอบจ่ายสินค้าจำนวนติดลบ"""
        result = self.inv.release_stock("P01", -5)
        self.assertFalse(result)
        self.assertEqual(self.p1.stock, 20)

    def test_stock_value_report(self):
        """ทดสอบการคำนวณรายงานมูลค่า"""
        report, total = self.inv.get_stock_value_report()
        self.assertEqual(total, 8000.0)

if __name__ == "__main__":
    unittest.main()