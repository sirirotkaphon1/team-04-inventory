import unittest
from inventory import inventory, add_item

class TestAddProduct(unittest.TestCase):

    def setUp(self):
        # รีเซ็ตค่าเริ่มต้นก่อนเริ่มการทดสอบแต่ละเคส
        inventory.clear()
        inventory.update({
            "item_001": {"name": "Laptop", "quantity": 10},
            "item_002": {"name": "Mouse", "quantity": 25}
        })

    # ทดสอบ AC-1: บันทึกสินค้าใหม่สำเร็จ
    def test_ac1_add_new_product_success(self):
        success, message = add_item("item_003", "Keyboard", 15)
        self.assertTrue(success)
        self.assertEqual(message, "บันทึกสินค้าสำเร็จ")
        self.assertIn("item_003", inventory)
        self.assertEqual(inventory["item_003"]["name"], "Keyboard")
        self.assertEqual(inventory["item_003"]["quantity"], 15)

    # ทดสอบ AC-2: ปฏิเสธเมื่อรหัสซ้ำ และไม่เขียนทับข้อมูลเดิม
    def test_ac2_duplicate_product_id(self):
        success, message = add_item("item_001", "New Laptop", 5)
        self.assertFalse(success)
        self.assertEqual(message, "รหัสสินค้าซ้ำ")
        self.assertEqual(inventory["item_001"]["name"], "Laptop")
        self.assertEqual(inventory["item_001"]["quantity"], 10)

if __name__ == "__main__":
    unittest.main()