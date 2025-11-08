from library import Library, Book, Member

def setup_library():
    """Khởi tạo thư viện với một số dữ liệu mẫu."""
    thu_vien = Library()
    thu_vien.add_book(Book(id="B001", author="Nguyễn Nhật Ánh", title="Mắt Biếc"))
    thu_vien.add_book(Book(id="B002", author="J.K. Rowling", title="Harry Potter và Hòn Đá Phù Thủy"))
    thu_vien.add_book(Book(id="B003", author="Dante Alighieri", title="Thần Khúc"))

    thu_vien.add_member(Member(id="M001", name="An Nguyễn"))
    thu_vien.add_member(Member(id="M002", name="Bình Trần"))

    return thu_vien


def handle_loan_book(library: Library):
    """Xử lý logic cho Lựa chọn 1: Mượn sách."""
    print("\n--- Mượn sách ---")
    member_id = input("Nhập ID thành viên (ví dụ: M001): ").strip().upper()
    book_id = input("Nhập ID sách (ví dụ: B001): ").strip().upper()
    library.loan_book(member_id, book_id)

def handle_return_book(library: Library):
    """Xử lý logic cho Lựa chọn 2: Trả sách."""
    print("\n--- Trả sách ---")
    member_id = input("Nhập ID thành viên: ").strip().upper()
    book_id = input("Nhập ID sách: ").strip().upper()
    library.return_book(member_id, book_id)

def handle_show_loans(library: Library):
    """Xử lý logic cho Lựa chọn 3: Thống kê."""
    print("\n--- Thống kê sách đang mượn ---")
    library.show_books_on_loan()
    print(f">>> Tổng số sách đang mượn: {library.count_books_on_loan()}")

def handle_show_all_books(library: Library):
    """Xử lý logic cho Lựa chọn 4: Hiển thị sách."""
    print("\n--- Danh sách sách trong kho ---")
    if not library.books:
        print("Chưa có sách nào.")
    else:
        for book in library.books.values():
            status = "Có sẵn" if book.is_available else "Đã được mượn"
            print(f"- {book} (Trạng thái: {status})")

def handle_show_all_members(library: Library):
    """Xử lý logic cho Lựa chọn 5: Hiển thị thành viên."""
    print("\n--- Danh sách thành viên ---")
    if not library.members:
        print("Chưa có thành viên nào.")
    else:
        for member in library.members.values():
            print(f"- {member}")

def add_new_book(library: Library):
    """Xử lý logic cho Lựa chọn 6: Thêm sách mới."""
    print("\n--- Thêm sách mới ---")
    try:
        book_id = input("Nhập ID sách mới (ví dụ: B100): ").strip().upper()
        title = input("Nhập tên sách: ").strip()
        author = input("Nhập tác giả: ").strip()

        if not book_id or not title or not author:
            print("Lỗi: ID, tên sách, và tác giả không được để trống.")
            return

        new_book = Book(id=book_id, author=author, title=title)
        library.add_book(new_book)
    except Exception as e:
        print(f"Đã xảy ra lỗi khi thêm sách: {e}")

def add_new_member(library: Library):
    """Xử lý logic cho Lựa chọn 7: Thêm thành viên mới."""
    print("\n--- Thêm thành viên mới ---")
    try:
        member_id = input("Nhập ID thành viên mới (ví dụ: M100): ").strip().upper()
        name = input("Nhập tên thành viên: ").strip()

        if not member_id or not name:
            print("Lỗi: ID và tên thành viên không được để trống.")
            return

        new_member = Member(id=member_id, name=name)
        library.add_member(new_member)
    except Exception as e:
        print(f"Đã xảy ra lỗi khi thêm thành viên: {e}")

def main_menu(library: Library):
    """Vòng lặp menu chính, gọi các hàm xử lý tương ứng."""
    while True:
        print("\n===== MENU QUẢN LÝ THƯ VIỆN =====")
        print("1. Mượn sách")
        print("2. Trả sách")
        print("3. Xem danh sách sách đang được mượn")
        print("---------------------------------------")
        print("4. Hiển thị tất cả sách trong thư viện")
        print("5. Hiển thị tất cả thành viên")
        print("---------------------------------------")
        print("6. Thêm một sách mới vào kho")
        print("7. Đăng ký thành viên mới")
        print("---------------------------------------")
        print("0. Thoát chương trình")
        print("========================================")
        
        choice = input("Vui lòng nhập lựa chọn của bạn: ")
        
        if choice == '1':
            handle_loan_book(library)
        elif choice == '2':
            handle_return_book(library)
        elif choice == '3':
            handle_show_loans(library)
        elif choice == '4':
            handle_show_all_books(library)
        elif choice == '5':
            handle_show_all_members(library)
        elif choice == '6':
            add_new_book(library)
        elif choice == '7':
            add_new_member(library)
        elif choice == '0':
            print("\nCảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break
        else:
            print("\nLỗi: Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        
        input("\n(Nhấn Enter để tiếp tục...)")


if __name__ == "__main__":
    thu_vien = setup_library()
    main_menu(thu_vien)