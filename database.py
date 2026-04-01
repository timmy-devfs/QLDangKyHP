import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv() # Load dữ liệu từ file .env

def connect_db():
    try:
        db = mysql.connector.connect(
            host=os.getenv("DB_SERVER"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT")) # Ép kiểu sang số nguyên
        )
        if db.is_connected():
            print("Kết nối database thành công!")
            return db
    except mysql.connector.Error as err:
        print(f"Lỗi kết nối: {err}")
        return None

connection = connect_db()
def setup_database():
    db = connect_db() 
    if not db:
        print("Không thể kết nối, dừng việc khởi tạo.")
        return

    cursor = db.cursor()
    try:
        schema_path = "database/schema.sql"
        seed_path = "database/seed_data.sql"

        # Bước 1: Đọc và chạy file schema.sql (Tạo các bảng)
        print("Đang tạo cấu trúc bảng...")
        with open(schema_path, 'r', encoding='utf-8') as f:
            # Tách các lệnh SQL bằng dấu chấm phẩy
            sql_commands = f.read().split(';')
            for cmd in sql_commands:
                if cmd.strip(): # Bỏ qua các khoảng trắng rỗng
                    cursor.execute(cmd)
        print("✅ Đã tạo các bảng từ schema.sql thành công!")

        # Bước 2: Đọc và chạy file seed_data.sql (Thêm dữ liệu mẫu)
        print("Đang thêm dữ liệu mẫu...")
        with open(seed_path, 'r', encoding='utf-8') as f:
            sql_commands = f.read().split(';')
            for cmd in sql_commands:
                if cmd.strip():
                    cursor.execute(cmd)
        print("✅ Đã thêm dữ liệu mẫu từ seed_data.sql thành công!")

        db.commit()

    except mysql.connector.Error as err:
        print(f"❌ Lỗi MySQL: {err}")
        db.rollback() 
    except FileNotFoundError as e:
        print(f"❌ Không tìm thấy file: {e}")
    finally:
        cursor.close()
        db.close()

if __name__ == "__main__":
    setup_database()