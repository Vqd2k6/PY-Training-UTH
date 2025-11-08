import datetime

class Book: 
    def __init__(self, id: str, author: str, title: str):
        self.id = id 
        self.author = author 
        self.title = title
        self.is_available = True 
    
    def __str__(self):
        return f"{self.title} của {self.author} (ID: {self.id})"

class Member:
    def __init__(self, id: str, name: str):
        self.id = id 
        self.name = name 

    def __str__(self):
        return f"Thành viên: {self.name} ({self.id})"

class Loan:
    def __init__(self, member_id: str, book_id: str):
        self.member_id = member_id
        self.book_id = book_id
        self.loan_date = datetime.date.today()
    
    def __repr__(self):
        return f"<Loan: {self.member_id} mượn {self.book_id} ngày {self.loan_date}>"

class Library:

    def __init__(self):
        self.books = {}     
        self.members = {}   
        self.loans = []     
    
    def add_book(self, book: Book):
        if book.id in self.books:
            print(f"Cảnh báo: Sách với ID {book.id} đã tồn tại.")
        else:
            self.books[book.id] = book
            print(f"Đã thêm sách: {book.title}")
    
    def add_member(self, member: Member):
        if member.id in self.members:
            print(f"Cảnh báo: Thành viên với ID {member.id} đã tồn tại.")
        else:
            self.members[member.id] = member
            print(f"Đã thêm thành viên: {member.name}")
    
    def loan_book(self, member_id, book_id):
        if member_id not in self.members:
            print(f"Lỗi mượn: Không tìm thấy thành viên ID {member_id}")
            return

        if book_id not in self.books:
            print(f"Lỗi mượn: Không tìm thấy sách ID {book_id}")
            return
        
        book_to_loan = self.books[book_id]
        if not book_to_loan.is_available:
            print(f"Lỗi mượn: Sách '{book_to_loan.title}' đã được mượn.")
            return

        book_to_loan.is_available = False
        new_loan = Loan(member_id, book_id)
        self.loans.append(new_loan)
    
        member_name = self.members[member_id].name
        print(f"Mượn thành công: {member_name} đã mượn sách '{book_to_loan.title}'.")


    def return_book(self, member_id, book_id):
        loan_to_remove = None
        
        for loan in self.loans:
            if loan.member_id == member_id and loan.book_id == book_id:
                loan_to_remove = loan
                break

        if loan_to_remove is not None:
            self.loans.remove(loan_to_remove)
            
            if book_id in self.books:
                self.books[book_id].is_available = True
            
            print(f"Trả sách thành công: Sách ID {book_id} đã được trả.")
        else:
            print("Lỗi trả: Không tìm thấy giao dịch mượn này.")

    def count_books_on_loan(self):
        return len(self.loans)

    def show_books_on_loan(self):
        if not self.loans:
            print("Hiện không có sách nào đang được mượn.")
            return

        print("--- Danh sách sách đang mượn ---")
        for loan in self.loans:
            book = self.books.get(loan.book_id)
            member = self.members.get(loan.member_id)
            
            if book and member: 
                print(f"- Sách: {book.title} (ID: {book.id})")
                print(f"  Mượn bởi: {member.name} (ID: {member.id})")
                print(f"  Ngày mượn: {loan.loan_date}")
            else:
                print(f"- Giao dịch lỗi: Không tìm thấy thông tin Book/Member cho {loan}")