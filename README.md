# N'Hilight chatbot
น้องไฮไลท์ เป็นแชทบอทที่ถูกสร้างขึ้นสำหรับใช้งานในโรงเรียน สามารถใช้งานได้ทั้งบุคคลภายนอก คุณครู และนักเรียน   

วีดีโอแนะนำ  
[![IMAGE ALT TEXT](https://img.youtube.com/vi/hb0PVw82esA/0.jpg)](https://www.youtube.com/watch?v=hb0PVw82esA "BOTNOI Chatbot Mara-Hackathon : Athena 🤖💫")

** หมายเหตุ 

1. สามารถเข้าทดลองใช้งานได้แอดไลน์ที่ Line ID : @518fquks  
2. สำหรับการทดสอบเข้าสู่ระบบ สามารถใช้ข้อมูลด้านล่างนี้เพื่อเข้าสู่ระบบ  
    นักเรียน  
    User: 10001  
    Password: pass  

    คุณครู  
    User: 10000  
    Password: password  

สำหรับการเปลี่ยน Account ที่ต้องการทดลอบ สามารถพิมพ์ Logout หาบอทเพื่อทำการ Logout

หมายเหตุ: แชทบอทนี้จัดทำเพื่อการแข่งขัน BOTNOI Marahackathon 2022 รอบคัดเลือก  

## Technical Detail 
ตัว API นั้นเขียนด้วยภาษา Python โดยใช้ Library FastAPI และ Host บน Google App Engine (สามารถนำ API ไป Run ที่อื่นได้ตามสะดวก) ส่วน Database เราใช้ Firebase Firestore   

ในการทดลอง Run  
1. สร้าง Firebase Project, เปิดใช้งาน Firestore และ Download file service account มาไว้ใน folder เดียวกับ file code (api)
2. แก้ชื่อ file service account ใน file main.py เป็น file ที่ download มา
3. ติดตั้ง Library ต่าง ๆ ตาม File requirement.txt  
4. Run ได้โดยใช้คำสั่ง  
```bash
uvicorn main:app
```
Note: หากจะนำไปใช้ผ่านตัว Chatbot โดย Run บนเครื่องอาจต้องมีการใช้ tunnel (เช่น ngrok, Cloudflare Tunnel) เพื่อให้สามารถเข้าถึงจากภายนอกได้  

ตัว Frontend ที่ใช้ Login นั้นเป็น Liff App ที่เรา Host โดยใช้ Github Pages แต่ว่าใช้ Custom Domain ทำให้ถ้าสังเกต URL จะไม่ใช้ github.io ซึ่งตรง url นี้จะต้องนำมาใช้ set CORS ใน file main.py โดยใส่ URL ของหน้า web login เข้าไป [(reference)](https://fastapi.tiangolo.com/tutorial/cors/)
