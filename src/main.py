from dataclasses import dataclass
from typing import List, Dict
from abc import ABC, abstractmethod

# --- Models ---

@dataclass
class Product:
    id: str
    name: str
    category: str
    price: float
    stock: int = 0
    threshold: int = 0

# --- Notification System (NFR-02: Maintainability) ---

class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass

class EmailNotification(NotificationChannel):
    def send(self, message: str) -> None:
        print(f"[Email Notification]: {message}")

class SMSNotification(NotificationChannel):
    def send(self, message: str) -> None:
        print(f"[SMS Notification]: {message}")

# --- Core Business Logic ---

class InventoryManager:
    def __init__(self):
        self.products: Dict[str, Product] = {}
        self.notification_channels: List[NotificationChannel] = []

    def add_product(self, product: Product) -> None:
        self.products[product.id] = product

    def register_notification_channel(self, channel: NotificationChannel) -> None:
        self.notification_channels.append(channel)

    def receive_stock(self, product_id: str, quantity: int) -> bool:
        """US-01: รับสินค้าเข้าสต็อก"""
        if quantity <= 0:
            print("Error: จำนวนสินค้าต้องมากกว่า 0")
            return False
        if product_id not in self.products:
            print("Error: ไม่พบสินค้า")
            return False

        self.products[product_id].stock += quantity
        print(f"รับเข้า {quantity}: {self.products[product_id].name} คงเหลือ {self.products[product_id].stock}")
        return True

    def release_stock(self, product_id: str, quantity: int) -> bool:
        """US-01, US-02: จ่ายสินค้าและแจ้งเตือนถ้าต่ำกว่า threshold"""
        if quantity <= 0:
            print("Error: จำนวนสินค้าต้องมากกว่า 0")
            return False

        product = self.products.get(product_id)
        if not product:
            print("Error: ไม่พบสินค้า")
            return False

        if product.stock < quantity:
            print(f"Error: สต็อกไม่พอ (มีอยู่ {product.stock})")
            return False

        product.stock -= quantity
        print(f"จ่ายออก {quantity}: {product.name} คงเหลือ {product.stock}")

        # AC ของ US-02: ตรวจสอบ Threshold (ต้องต่ำกว่าเท่านั้น)
        if product.stock < product.threshold:
            self._notify_manager(f"สินค้า {product.name} ต่ำกว่ากำหนด! (เหลือ {product.stock}, กำหนด {product.threshold})")

        return True

    def _notify_manager(self, message: str) -> None:
        """NFR-03: Reliability - แจ้งเตือนล้มเหลวต้องไม่กระทบ Transaction หลัก"""
        for channel in self.notification_channels:
            try:
                channel.send(message)
            except Exception as e:
                print(f"Log Error: ส่งแจ้งเตือนผ่าน {type(channel).__name__} ล้มเหลว: {e}")

    def get_stock_value_report(self):
        """US-03, FR-04: รายงานมูลค่าสต็อกแยกตามหมวดหมู่"""
        category_report = {}
        total_value = 0.0

        for p in self.products.values():
            value = p.stock * p.price
            category_report[p.category] = category_report.get(p.category, 0.0) + value
            total_value += value

        print("\n--- รายงานมูลค่าสต็อก ---")
        for cat, val in category_report.items():
            print(f"{cat}: {val:,.2f} บาท")
        print(f"รวมทั้งหมด: {total_value:,.2f} บาท")
        print("----------------------\n")
        return category_report, total_value

if __name__ == "__main__":
    inv = InventoryManager()

    inv.register_notification_channel(EmailNotification())

    p1 = Product(id="P01", name="สายไฟ 2.5 sq.mm", category="งานไฟฟ้า", price=250.0, stock=20, threshold=15)
    p2 = Product(id="P02", name="ท่อ PVC 1 นิ้ว", category="งานประปา", price=300.0, stock=10, threshold=5)
    inv.add_product(p1)
    inv.add_product(p2)

    print("--- ทดสอบ AC ของ US-02 (Low Stock Alert) ---")
    inv.release_stock("P01", 8)  # เหลือ 12 (<15) -> เตือน

    print("\n--- ทดสอบ Edge Case (จ่ายเท่ากับ Threshold พอดี) ---")
    inv.receive_stock("P01", 8)   # คืนสต็อกเป็น 20
    inv.release_stock("P01", 5)  # เหลือ 15 (=15) -> ไม่เตือน

    print("\n--- ทดสอบ AC ของ US-01 (Inventory Update & Validation) ---")
    inv.release_stock("P02", 15) # สต็อกไม่พอ
    inv.release_stock("P02", -5) # จำนวนไม่ถูกต้อง

    print("\n--- ทดสอบ AC ของ US-03 (Value Report) ---")
    inv.get_stock_value_report()