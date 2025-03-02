## วิธีรัน Test Cases และตรวจสอบ Coverage

### การรัน Test Cases

1. **รัน test cases แบบ verbose (แสดงผลลัพธ์แบบละเอียด)**:
   ```bash
   python -m unittest -v {filename}
   ```

### การตรวจสอบ Coverage

1. **รัน test cases พร้อมตรวจสอบ coverage**:
   ```bash
   coverage run -m unittest {filename}
   ```

2. **สร้างรายงาน coverage แบบ text**:
   ```bash
   coverage report -m
   ```

3. **(Optional) สร้างรายงาน coverage แบบ HTML**:
   ```bash
   coverage html
   ```
   - เปิดไฟล์ `htmlcov/index.html` ในเบราว์เซอร์เพื่อดูรายงาน coverage แบบกราฟิก
```

