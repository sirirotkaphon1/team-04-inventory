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
# --- ฟังก์ชันเพิ่มสินค้าใหม่ (US-02) ---
def add_item(item_id, name, quantity):
    if quantity < 0:
        return False, "จำนวนสินค้าต้องเป็น 0 หรือมากกว่า"

    # AC-2: ตรวจสอบรหัสสินค้าซ้ำ
    if item_id in inventory:
        return False, "รหัสสินค้าซ้ำ"

    # AC-1: บันทึกสินค้าใหม่
    inventory[item_id] = {
        "name": name,
        "quantity": quantity
    }
    return True, "บันทึกสินค้าสำเร็จ"