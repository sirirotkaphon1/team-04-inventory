# Sprint Retrospective: Sprint 1 (team-04-inventory)

## Velocity
- Story point ที่วางแผน: 9 (US-01 รวม 3 แต้ม, US-02 รวม 3 แต้ม, US-03 รวม 3 แต้ม)
- Story point ที่ทำสำเร็จ (Done): 9
- Velocity Sprint 1: 9 points

## เพดานงานที่ทำพร้อมกัน (WIP limit)
- เพดานที่ตั้งไว้ใน TEAM_CHARTER.md: 2 ใบ
- ชนเพดานกี่ครั้งใน sprint นี้: 0 ครั้ง (ทุกคนรับงานทีละ 1 ใบ ไม่เกินที่ตั้งไว้)
- เพดานที่จะใช้ใน sprint หน้า: 2 ใบ เพราะเหมาะสมกับจำนวนสมาชิกในทีม ช่วยให้โฟกัสงานและตรวจ Review ได้ละเอียด

## Start: สิ่งที่ควรเริ่มทำในรอบต่อไป
1. ควรตรวจสอบตำแหน่งโฟลเดอร์ (Directory Path) และสลับ Branch ให้ถูกต้องใน Terminal ก่อนพิมพ์คำสั่ง Git ทุกครั้ง
2. ควรตกลงและแจกจ่ายงานในแต่ละ User Story ให้สมาชิกในทีมอย่างชัดเจนตั้งแต่เริ่มเปิด Sprint

## Stop: สิ่งที่ควรหยุดทำ
1. หยุดพิมพ์คำสั่ง git add และ git commit โดยที่ยังไม่ได้กดบันทึกไฟล์ (Ctrl + S) ใน VS Code
2. หยุดการรันคำสั่ง Git ในโฟลเดอร์ที่ซ้อนกันอยู่โดยไม่เช็ก pwd หรือ cd ให้ดีก่อน

## Continue: สิ่งที่ทำได้ดี ควรทำต่อ
1. การช่วยกันรีวิวโค้ดและคอมเมนต์ตรวจสอบใน Pull Request (PR) ก่อนกด Merge เข้าสายหลัก main
2. การอัปเดตสถานะ Issue และการ์ดใน GitHub Projects ให้เป็นสถานะ Done เมื่อสปรินต์งานเสร็จสมบูรณ์

## AI Commit Audit
- PR ของ US-02 และ US-03: ข้อความ Commit ในช่วงแรกอธิบายเพียงสั้นๆ ทีมได้ปรับแก้ข้อความตามแนวทางที่ AI แนะนำ โดยระบุวัตถุประสงค์ (Why) เช่น การอัปเดตฟังก์ชัน add_item และ update_stock ในไฟล์ inventory.py เพื่อให้ตรงตามมาตรฐาน Conventional Commits

## Action Item สำหรับ Sprint ถัดไป
| Action | เจ้าของ |
|---|---|
| ทบทวนคำสั่ง Git ขั้นพื้นฐาน และการเช็กความถูกต้องของ Directory ก่อน Commit | ทุกคนในทีม |
| ศึกษาการเขียน Unit Test เพื่อทดสอบฟังก์ชันในไฟล์ inventory.py | สมาชิกผู้พัฒนาโค้ด |
<img width="1917" height="874" alt="image" src="https://github.com/user-attachments/assets/0115da98-8490-409b-b55a-6a7eff043e80" />
