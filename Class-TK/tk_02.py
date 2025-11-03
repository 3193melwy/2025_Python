import tkinter as tk

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def borrow(self):
        self.borrowed = True
        return f'"{self.title}"(이)가 대출되었습니다.'

    def return_book(self):
        self.borrowed = False
        return f'"{self.title}"(이)가 반납되었습니다.'

    def equals(self, title, author):
        return self.title == title and self.author == author

borrowed_books = []

def update_borrowed_list():
    if borrowed_books:
        book_list_str = "\n".join([f"• {b.title} - {b.author}" for b in borrowed_books])
    else:
        book_list_str = "현재 대출 중인 도서가 없습니다."
    borrowed_list_label.config(text=book_list_str)

def set_message(text, color):
    result_label.config(text=text, fg=color)

def handle_borrow():
    title = title_entry.get().strip()
    author = author_entry.get().strip()

    if not title or not author:
        set_message("제목 또는 저자가 비어 있습니다. (오류)", "red")
        return

    for book in borrowed_books:
        if book.equals(title, author):
            set_message(f'"{title}"(은/는) 이미 대출 중입니다. (중복 오류)', "red")
            return

    new_book = Book(title, author)
    message = new_book.borrow()
    borrowed_books.append(new_book)
    set_message(message, "blue")
    update_borrowed_list()

def handle_return():
    title = title_entry.get().strip()
    author = author_entry.get().strip()

    book_to_return = None
    for book in borrowed_books:
        if book.equals(title, author):
            book_to_return = book
            break

    if book_to_return:
        borrowed_books.remove(book_to_return)
        message = book_to_return.return_book()
        set_message(message, "green")
    else:
        set_message(f'"{title}"(은/는) 대출 목록에 없습니다.', "red")

    update_borrowed_list()

root = tk.Tk()
root.title("도서 관리 프로그램")
root.geometry("460x320")
root.resizable(False, False)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="제목:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
title_entry = tk.Entry(input_frame, width=30)
title_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="저자:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
author_entry = tk.Entry(input_frame, width=30)
author_entry.grid(row=1, column=1, padx=5, pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

borrow_button = tk.Button(button_frame, text="대출", command=handle_borrow, width=15)
borrow_button.grid(row=0, column=0, padx=10)

return_button = tk.Button(button_frame, text="반납", command=handle_return, width=15)
return_button.grid(row=0, column=1, padx=10)

result_label = tk.Label(root, text="결과 및 메시지", fg="black", font=('Arial', 10))
result_label.pack(pady=5)

status_frame = tk.Frame(root)
status_frame.pack(pady=10, fill='x', padx=10)

tk.Label(status_frame, text="[현재 대출 현황]", font=('Arial', 10, 'bold')).pack(anchor='w')
borrowed_list_label = tk.Label(status_frame, text="현재 대출 중인 도서가 없습니다.", justify=tk.LEFT, anchor='w')
borrowed_list_label.pack(anchor='w')

update_borrowed_list()
root.mainloop()
