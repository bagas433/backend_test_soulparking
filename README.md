# backend_test_soulparking
code testing for soul parking by bagaskara P

## Installation

### Python version
Untuk python version yang digunakan saat membuat API ini adalah versi 3.8.8, namun untuk python version 3.6 > sudah bisa berjalan 
### Library
Untuk daftar library-library apa saja yang dibutuhkan, bisa di install dengan menjalankan requirements.txt yang tersedia di folder requirement

```bash
pip install -r requirements.txt
```

---


## Penggunaan API

### Testing API
Untuk menggunakan API pertama kita bisa menjalankan API tersebut dengan script python berikut

```python
python app.py
```

untuk daftar endpoint yang tersedia adalah sebagai berikut:
- localhost:5000/todo ( POST )  # MEMBUAT TODO LIST
- localhost:5000/todo ( GET )   # MENDAPATKAN ALL TODO LIST
- localhost:5000/todo/<todo_id> ( GET ) # MENDAPATKAN DETAIL TODO LIST
- localhost:5000/todo/<todo_id> ( PUT/PATCH ) # MENGUPDATE TODO LIST
- localhost:5000/todo/<todo_id> ( DELETE )  # MENGHAPUS TODO LIST
- localhost:5000/todo/<todo_id> ( POST )    # MENYELESAIKAN TODO LIST

