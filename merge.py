import json

# ชื่อไฟล์ทั้งหมดที่ต้องการรวม
files = ['tarot-major.json', 'tarot-wands-cups.json', 'tarot-swords-pentacles.json']
all_cards = []

# โหลดข้อมูลจากทีละไฟล์
for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        all_cards.extend(data['cards'])

# เรียงตาม ID
all_cards.sort(key=lambda x: x['id'])

# เซฟเป็นไฟล์ใหม่
with open('tarot-all.json', 'w', encoding='utf-8') as f:
    json.dump({"cards": all_cards}, f, ensure_ascii=False, indent=2)

print("รวมไฟล์เสร็จเรียบร้อย! สร้างไฟล์ tarot-all.json แล้ว")