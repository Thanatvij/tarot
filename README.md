# 🔮 พยากรณ์แห่งดวงดาว

> เว็บไซต์ดูดวงไพ่ทาโรต์ภาษาไทย — ใช้ภาพจริงจาก Rider-Waite-Smith deck (1909, Public Domain)

## 🌐 Live Demo

**👉 [คลิกที่นี่เพื่อเปิดเว็บ](https://thanatvij.github.io/tarot/)**

---

## ✨ ฟีเจอร์

- 🃏 **ไพ่ทาโรต์ครบ 78 ใบ** — Major Arcana 22 ใบ + Minor Arcana 56 ใบ (Wands/Cups/Swords/Pentacles)
- 🎴 **ภาพไพ่จริง** — Rider-Waite-Smith Tarot โดย Pamela Colman Smith (1909, Public Domain)
- 🌓 **เรียงไพ่เป็นพัดครึ่งวงกลม** — สวยขลัง ตามแบบหมอดูดั้งเดิม ด้วย CSS transforms
- 📱 **Responsive Design** — รองรับทุกอุปกรณ์ ด้วย Tailwind CSS + Custom CSS
- 🎯 **เลือกหมวดได้ 5 หมวด** — ความรัก / การเรียน / การทำงาน / การเงิน / ดวงชะตาภาพรวม
- 🔮 **อ่านไพ่ 3 ตำแหน่ง** — เจ้าชะตา → สถานการณ์ → บทสรุป
- ✨ **คำพยากรณ์รวม** — วิเคราะห์ภาพรวมจากจำนวน Major Arcana และชุดไพ่ที่ปรากฏซ้ำ
- 🎨 **ดีไซน์ขลังลึกลับ** — โทนม่วง+ทอง พร้อม animation, ดาวระยิบระยับ, พระจันทร์เรืองแสง

---

## 🚀 วิธีใช้งาน

### เปิดในเครื่อง (Local Development)

```bash
# วิธีที่ 1: เปิดตรงๆ (ต้องต่อเน็ตเพื่อโหลดรูปไพ่จาก CDN)
open index.html

# วิธีที่ 2: รัน server (แนะนำ)
python3 -m http.server 8000
# จากนั้นเปิด http://localhost:8000
```

### วิธีดูดวง

1. กดปุ่ม **"เริ่มเปิดไพ่"**
2. เลือกหมวดที่ต้องการพยากรณ์ (ความรัก / การเรียน / การทำงาน / การเงิน / ดวงชะตาภาพรวม)
3. ระบุคำถามเพิ่มเติม (ถ้ามี) — ไม่จำเป็น
4. **เลือกไพ่ 3 ใบจากพัดครึ่งวงกลม** — คลิกที่ไพ่ที่สะดุดตา
5. รับคำพยากรณ์จากจักรวาล ✨

---

## 🛠 เทคโนโลยี

### Core Technologies
- **HTML5** — โครงสร้างหน้าเว็บ
- **CSS3** — ดีไซน์ + animation 3D + พัดครึ่งวงกลม (CSS transforms)
- **Tailwind CSS** — Responsive utilities (ผ่าน CDN, ไม่ต้อง build)
- **Vanilla JavaScript** — ไม่ใช้ framework
- **Google Fonts** — Cinzel, Noto Serif Thai, Sarabun
- **jsDelivr CDN** — โหลดรูปไพ่ Rider-Waite (Public Domain) จาก npm package `tarot-card-img`

### ไม่มีอะไรเหล่านี้
❌ ไม่ใช้ external API  
❌ ไม่ใช้ localStorage  
❌ ไม่ต้อง build step  
❌ ไม่ต้อง install dependencies  
✅ ทำงาน offline ได้เกือบหมด (ยกเว้นรูปไพ่ที่โหลดจาก CDN)

---

## 📂 โครงสร้างไฟล์

```
tarot-web/
├── index.html           # ไฟล์เว็บหลัก (HTML + Tailwind CDN)
├── css/
│   └── style.css        # Custom CSS (effects, card fan, animations)
├── js/
│   └── app.js           # Card logic, state management, readings
├── tarot-all.json       # ข้อมูลไพ่ 78 ใบ + ความหมายทุกหมวด
├── README.md            # ไฟล์นี้
├── CLAUDE.md            # Project documentation สำหรับ Claude Code
└── .gitignore           # กันไฟล์ที่ไม่ควรขึ้น GitHub
```

---

## 🎴 ระบบการอ่านไพ่

### การเรียงไพ่ (Card Spread)
เรียงไพ่แบบ **พัดครึ่งวงกลม (Semi-Circular Fan)** โดยใช้ CSS transforms:
- ไพ่ 78 ใบกระจายเป็นพัดมุม 160°
- ไพ่แต่ละใบมีการคำนวณ position ด้วย JavaScript
- Responsive radius — ปรับขนาดตามหน้าจอ (220px → 160px → 115px → 95px)

### ตำแหน่งไพ่ 3 ใบ (3-Card Spread)
1. **เจ้าชะตา (The Seeker)** — ตัวคุณ บุคลิก พลังงานในตัว
2. **สถานการณ์ (The Situation)** — สิ่งที่กำลังเผชิญ ปัจจัยรอบข้าง
3. **บทสรุป (The Outcome)** — ผลลัพธ์ คำชี้แนะ แนวทาง

### หมวดที่เลือกได้ (Categories)
| หมวด | Emoji | ความหมาย |
|-------|-------|----------|
| ความรัก | 💕 | เรื่องรัก ความสัมพันธ์ คู่ |
| การเรียน | 📚 | การศึกษา การเรียนรู้ การสอบ |
| การทำงาน | 💼 | งาน อาชีพ โอกาสใหม่ |
| การเงิน | 💰 | เงิน โชคลาภ การลงทุน |
| ดวงชะตาภาพรวม | 🌟 | ดวงชะตาโดยรวม แนวโลคทั่วไป |

---

## 📚 แหล่งข้อมูลและเครดิต

### ภาพไพ่ (Card Images)
**Rider-Waite-Smith Tarot Deck (1909)** by Pamela Colman Smith และ Arthur Edward Waite

- **สถานะลิขสิทธิ์**: Public Domain
  - US: หมดลิขสิทธิ์ตั้งแต่ปี 1966
  - UK: หมดลิขสิทธิ์ตั้งแต่ปี 2022
- **แหล่งที่มา**: โหลดผ่าน jsDelivr CDN จาก npm package `tarot-card-img`

### ความหมายไพ่ (Card Meanings)
อ้างอิงจาก:
- ตำราไพ่ทาโรต์ไทย
- *The Pictorial Key to the Tarot* โดย A. E. Waite (1911, Public Domain)

---

## 👤 ผู้พักษนา

**Thanat**  
DTI (Digital Technology and Innovation), Thammasat University Lampang

📷 Instagram: [@thanxt.v](https://instagram.com/thanxt.v)

---

## 📝 License

เว็บไซต์นี้เป็นโอเพนซอร์ส สร้างด้วย ❤️ เพื่อชุมชน

รูปไพ่เป็น Public Domain — สามารถนำไปใช้ได้โดยไม่มีค่าใช้จ่าย

---

> _ติดต่อสำหรับการดูดวงเชิงลึกเพิ่มเติม_
