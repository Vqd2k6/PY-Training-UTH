# Bài Tập và Dự Án Mini - Python Basic 2 (Jupyter Notebook)

### Giới thiệu chung
Tập hợp này chứa các bài tập thực hành cơ bản của Python, được thiết kế để chạy và tương tác trực tiếp trong môi trường **Jupyter Notebook** (hoặc Google Colab).

Các chủ đề chính bao gồm: **Cấu trúc điều kiện/vòng lặp**, **Dictionary/Set**, và **Comprehension** (list/dict/set). Mục tiêu là nắm vững các cấu trúc dữ liệu cơ bản và các kỹ thuật viết code ngắn gọn, hiệu quả trong Python.

---

### Cấu trúc và Cách sử dụng
Toàn bộ mã nguồn và kết quả chạy được chứa trong một file Notebook duy nhất.

1.  **Môi trường**: Mở file **`exercise.ipynb`** trong **Jupyter Notebook** hoặc **Google Colab**.
2.  **Chạy Code**: Chạy từng ô (cell) theo thứ tự để xem lời giải và kết quả của từng bài tập.

---

### Nội dung các Bài tập (8 bài)

| Bài tập | Chủ đề Chính | Mô tả |
| :--- | :--- | :--- |
| **Bài 1** | **Dictionary** | **Word Count**: Đếm tần suất từ trong văn bản (bỏ dấu câu, lower-case). |
| **Bài 2** | **Nested Loops** | Tạo bảng cửu chương 1..9 bằng vòng lặp lồng nhau. |
| **Bài 3** | **Set** | Tách các từ duy nhất từ câu và in theo thứ tự alphabet dùng `set`. |
| **Bài 4** | **Dictionary** | Chuyển danh sách (list) sinh viên dạng dictionary sang dictionary nhóm theo lớp (`class`). |
| **Bài 5** | **Sắp xếp** | Sắp xếp danh sách từ theo độ dài, nếu bằng nhau thì sắp xếp theo alphabet. |
| **Bài 6** | **List Comprehension** | Sinh list bình phương các số lẻ từ 1..n bằng list comprehension. |
| **Bài 7** | **Nested Loops** | Tạo ma trận n x n danh số... |
| **Bài 8** | **Hàm Built-in** | Sử dụng các hàm built-in (`enumerate`, `zip`, `any/all`, `sum`, `min/max`). |

---

### Dự án Mini - Trình Đọc Log

Dự án nhỏ này tập trung vào kỹ năng làm việc với **File I/O** và **Dictionary** trong Python.

#### Chức năng
* **Đọc File**: Chương trình đọc một file log dạng `.txt` (cần phải tạo file `log.txt` tương ứng trong cùng thư mục).
* **Phân tích Log**: Xử lý từng dòng log, bỏ qua các dòng không hợp lệ hoặc trống.
* **Thống kê Lỗi**: Đếm tần suất xuất hiện của các cấp độ log mục tiêu (`INFO`, `WARN`, `ERROR`).
* **Output**: In ra một dictionary chứa thống kê cuối cùng.

---

### Tác giả
-   **Tên**: Võ Quang Dũng
-   **Liên hệ**: Vqd2k6@gmail.com