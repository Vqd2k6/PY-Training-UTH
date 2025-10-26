# Mini Project - Quản lý Chi tiêu Cá nhân (Jupyter Notebook)

### Giới thiệu chung
Đây là một chương trình **Quản lý Chi tiêu Cá nhân** đơn giản, được thiết kế để chạy trong môi trường **Jupyter Notebook** (hoặc Google Colab). Chương trình cho phép người dùng nhập các giao dịch thu/chi, phân loại theo danh mục và xuất ra các báo cáo tổng kết cơ bản ngay trong các ô (cell) của Notebook.

Dự án được phát triển bằng **Python 3.x** và sử dụng module **`datetime`** tiêu chuẩn để xử lý ngày tháng.

---

### Cách sử dụng (Chạy chương trình)
Vì đây là file Notebook, bạn cần chạy từng ô (cell) theo thứ tự để khởi tạo và tương tác với chương trình.

1.  **Môi trường**: Mở file `.ipynb` trong **Jupyter Notebook** hoặc **Google Colab**.
2.  **Chạy các hàm**: Chạy các ô code định nghĩa các hàm (`them_giao_dich`, `tong_ket_theo_danh_muc`, `xuat_bao_cao`).
3.  **Khởi chạy Menu**: Chạy ô code chứa hàm `main()`.

Sau khi chạy `main()`, bạn sẽ thấy Menu chính hiện ra. Chương trình sẽ chờ bạn nhập lựa chọn vào ô `input()`:

---

### Các Chức năng chính

| Lựa chọn | Tên Chức năng | Mô tả chi tiết |
| :--- | :--- | :--- |
| **1** | Thêm giao dịch mới | Cho phép nhập **Ngày** (`YYYY-mm-dd`), **Loại** (`Thu/Chi`), **Số tiền** và **Danh mục**. Dữ liệu được lưu trong danh sách (`danh_sach_giao_dich`) trong bộ nhớ tạm (in-memory). |
| **2** | Thống kê theo danh mục | Tính toán và in ra tổng số tiền Thu và Chi cho mỗi danh mục đã nhập. |
| **3** | Xuất báo cáo chi tiết | Hiển thị toàn bộ danh sách giao dịch. Sau đó, tính và in ra **Tổng thu**, **Tổng chi** và **Ngân sách còn lại**. |
| **0** | Thoát | Kết thúc chương trình. |

---

### Lưu ý quan trọng
* **Dữ liệu In-Memory**: Các giao dịch chỉ được lưu trữ trong biến `danh_sach_giao_dich` khi chương trình đang chạy trong Notebook. Nếu bạn tắt Kernel hoặc khởi động lại Notebook, dữ liệu sẽ bị mất.
* **Format Ngày tháng**: Yêu cầu nhập ngày theo định dạng chính xác: `YYYY-mm-dd`.

---

### Tác giả
-   **Tên**: Võ Quang Dũng
-   **Liên hệ**: vqd2k6@gmail.com