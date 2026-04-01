import tkinter as tk
from tkinter import ttk, messagebox
from database import connect_db # Import hàm kết nối từ file database.py của bạn

class AppQLHP:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống Quản lý Đăng ký Học phần - TV02")
        self.root.geometry("800x500")

        # 1. Tiêu đề
        title = tk.Label(self.root, text="DANH SÁCH HỌC PHẦN HIỆN CÓ", font=("Arial", 16, "bold"), pady=20)
        title.pack()

        # 2. Khung chứa bảng (Treeview)
        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Định nghĩa các cột
        columns = ("ma_hp", "ten_hp", "so_tin_chi", "hoc_phi")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings")

        # Đặt tiêu đề cho từng cột
        self.tree.heading("ma_hp", text="Mã Học Phần")
        self.tree.heading("ten_hp", text="Tên Môn Học")
        self.tree.heading("so_tin_chi", text="Số Tín Chỉ")
        self.tree.heading("hoc_phi", text="Học Phí (VNĐ)")

        # Căn chỉnh độ rộng cột
        self.tree.column("ma_hp", width=100, anchor="center")
        self.tree.column("ten_hp", width=300)
        self.tree.column("so_tin_chi", width=100, anchor="center")
        self.tree.column("hoc_phi", width=150, anchor="e")

        # Thêm thanh cuộn (Scrollbar)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # 3. Nút bấm thao tác
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        btn_load = tk.Button(btn_frame, text="Tải dữ liệu", command=self.load_data, bg="#2196F3", fg="white", padx=20)
        btn_load.pack(side="left", padx=10)

        btn_exit = tk.Button(btn_frame, text="Thoát", command=root.quit, bg="#f44336", fg="white", padx=20)
        btn_exit.pack(side="left", padx=10)

    # 4. Hàm lấy dữ liệu từ MySQL đổ vào bảng
    def load_data(self):
        # Xóa dữ liệu cũ trên bảng trước khi nạp mới
        for item in self.tree.get_children():
            self.tree.delete(item)

        db = connect_db()
        if db:
            cursor = db.cursor()
            try:
                # Truy vấn bảng hoc_phan (đảm bảo tên bảng khớp với schema.sql của bạn)
                cursor.execute("SELECT ma_hp, ten_hp, so_tin_chi, hoc_phi FROM hoc_phan")
                rows = cursor.fetchall()
                
                for row in rows:
                    self.tree.insert("", "end", values=row)
                
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể lấy dữ liệu: {e}")
            finally:
                db.close()
        else:
            messagebox.showwarning("Thông báo", "Chưa kết nối được Database!")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppQLHP(root)
    root.mainloop()