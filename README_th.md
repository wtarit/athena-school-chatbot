[English](https://github.com/wtarit/athena-school-chatbot/blob/main/README.md)
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
ตัว API นั้นเขียนด้วย Python โดยใช้ FastAPI และ Firebase Firestore สำหรับเก็บข้อมูลผู้ใช้ ตัว API Host อยู่บน Vercel (สามารถนำ API ไป Run ที่อื่นได้ตามสะดวก)   

ในการทดลอง Run  
1. สร้าง Firebase Project, เปิดใช้งาน Firestore และ Download file service account
2. แก้ชื่อ file service account ใน file main.py เป็น file ที่ download มา
3. Run `pip install -r requirement.txt` เพื่อติดตั้ง Library 
4. Run ได้โดยใช้คำสั่ง  
```bash
uvicorn main:app
```
Note: หากจะนำไปใช้ผ่านตัว Chatbot โดย Run บนเครื่องอาจต้องมีการใช้ tunnel (เช่น ngrok, Cloudflare Tunnel) เพื่อให้สามารถเข้าถึงจากภายนอกได้  

ตัว Frontend ที่ใช้ Login นั้นเป็น Liff App ที่เรา Host โดยใช้ Github Pages โดยให้นำ URL ของหน้า web login มาใส่ใน file `.env` เพื่อ set CORS Origin [(reference)](https://fastapi.tiangolo.com/tutorial/cors/)

## Flow การทำงานการ Login
ในการ Login เราใช้วิธีให้ Login ในหน้า Web ที่เป็น Liff app ซึ่งสามารถเก็บ UserID ของ Line และส่ง Message ได้  

ซึ่งเราจึงทำเป็น form login ในหน้า web แล้วเก็บ UserID ด้วย ถ้า Login สำเร็จ เราก็จะเก็บข้อมูล UserID ไว้ใน Database และส่ง Message "Login" เข้าไปใน Chat โดยใน Botnoi ก็จะสร้าง Intent เพื่อจับ Keyword นี้ไว้ และ Intent นี้ก็จะทำการเรียก API เพื่อ check UserID ถ้า UserID ตรงกับที่มีการลงทะเบียนไว้ก็จะ return เป็นอีก Intent หนึ่ง ที่จะใช้เปลี่ยน Rich Menu เป็น Menu สำหรับผู้ที่ Login แล้ว (เนื่องจาก API ไม่สามารถ Return object Rich Menu ได้โดยตรง เลยต้องทำผ่านอีก Intent หนึ่ง)
