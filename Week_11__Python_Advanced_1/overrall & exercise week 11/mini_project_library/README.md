# Simple Library Management System - Chương trình Quản lý Thư viện (Python OOP CLI)

### Giới thiệu chung
Đây là một ứng dụng **Quản lý Thư viện** đơn giản, được xây dựng bằng Python và áp dụng các nguyên tắc **Lập trình Hướng đối tượng (OOP)**. Chương trình hoạt động dưới dạng giao diện dòng lệnh (CLI) với đầy đủ các chức năng cơ bản như thêm sách, thêm thành viên, mượn/trả sách, và thống kê.

Dự án sử dụng các **Class** (`Book`, `Member`, `Loan`, `Library`) để mô hình hóa các thực thể trong hệ thống thư viện.

---


### Cách cài đặt và chạy
Chương trình không yêu cầu thư viện bên ngoài và chạy trực tiếp bằng trình thông dịch Python.

1.  **Yêu cầu**: Cần có **Python 3.x** đã được cài đặt trên máy.
2.  **Chạy Chương trình**:
    Mở Terminal/Command Prompt, điều hướng đến thư mục chứa các file code và chạy lệnh sau:
    ```bash
    python main.py
    ```

3.  **Dữ liệu Mẫu**: Chương trình sẽ tự động khởi tạo với một số sách và thành viên mẫu để bạn có thể bắt đầu thử nghiệm ngay lập tức.

---

### Các Chức năng chính (Menu)
Chương trình cung cấp một menu chính (với 7 lựa chọn) để quản lý các tác vụ thư viện:

| Lựa chọn | Tên Chức năng | Class/Hàm Phụ trách |
| :--- | :--- | :--- |
| **1** | Mượn sách | `Library.loan_book` |
| **2** | Trả sách | `Library.return_book` |
| **3** | Xem sách đang mượn | `Library.show_books_on_loan` |
| **4** | Hiển thị tất cả sách | `Library.books` (danh sách) |
| **5** | Hiển thị tất cả thành viên | `Library.members` (danh sách) |
| **6** | Thêm sách mới | `Library.add_book` |
| **7** | Đăng ký thành viên mới | `Library.add_member` |
| **0** | Thoát chương trình | Kết thúc vòng lặp `while` |

---

### Các Class (Mô hình OOP)

| Class | Mô tả |
| :--- | :--- |
| **`Book`** | Đại diện cho một cuốn sách. Có thuộc tính `id`, `author`, `title` và trạng thái `is_available`. |
| **`Member`** | Đại diện cho một thành viên. Có thuộc tính `id` và `name`. |
| **`Loan`** | Đại diện cho một giao dịch mượn sách. Lưu trữ `member_id`, `book_id` và `loan_date`. |
| **`Library`** | Class trung tâm, quản lý các dictionary (`books`, `members`) và danh sách (`loans`). Chứa các phương thức xử lý nghiệp vụ chính. |

---

### Tác giả
-   **Tên**: Võ Quang Dũng
-   **Liên hệ**: Vqd2k6@gmail.com