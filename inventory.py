inventory = {
    "item_001": {"name": "Laptop", "quantity": 10},
    "item_002": {"name": "Mouse", "quantity": 25}
}

def update_stock(item_id, change_quantity):
    """
    ฟังก์ชันสำหรับปรับ/แก้ไขจำนวนสินค้า (รับเข้า หรือ จ่ายออก)
    - change_quantity เป็นบวก (+) เมื่อรับสินค้าเข้า
    - change_quantity เป็นลบ (-) เมื่อจ่ายสินค้าออก
    """
    if item_id in inventory:
        new_quantity = inventory[item_id]["quantity"] + change_quantity
        
        # ตรวจสอบไม่ให้จำนวนสินค้าติดลบ
        if new_quantity < 0:
            print(f"Error: จำนวนสินค้าคงเหลือไม่พอ (มีอยู่ {inventory[item_id]['quantity']})")
            return False
            
        inventory[item_id]["quantity"] = new_quantity
        print(f"อัปเดตเรียบร้อย: {inventory[item_id]['name']} คงเหลือ {new_quantity} ชิ้น")
        return True
    else:
        print("Error: ไม่พบรหัสสินค้านี้ในระบบ")
        return False

# ตัวอย่างการทดสอบใช้งาน
if __name__ == "__main__":
    update_stock("item_001", 5)   # รับเข้า 5 ชิ้น
    update_stock("item_002", -3)  # จ่ายออก 3 ชิ้น