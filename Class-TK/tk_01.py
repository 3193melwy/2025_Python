import tkinter as tk
from tkinter import messagebox


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False
    

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            return f'"{self.title}"(이)가 대출되었습니다.'
        else:
            return f'"{self.title}"(은/는) 이미 대출 중입니다.'

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            return f'"{self.title}"(이)가 반납되었습니다.'
        else:
            return f'"{self.title}"(은/는) 대출되지 않은 상태입니다.'
            
current_book = None 


def handle_borrow():
    global current_book
    title = title_entry.get().strip()
    author = author_entry.get().strip()
    
    if not title or not author:
        result_label.config(text="제목과 저자를 입력해주세요.")
        return

    current_book = Book(title, author)
    message = current_book.borrow()
    result_label.config(text=message)

def handle_return():
    global current_book
    
    if current_book is None:
        result_label.config(text="대출할 책이 먼저 선택되어야 합니다.")
        return
        
    message = current_book.return_book()
    result_label.config(text=message)


root = tk.Tk()
root.title("도서 대출 관리 프로그램")

root.columnconfigure(0, weight=1) 
root.columnconfigure(2, weight=1)

tk.Label(root, text="제목:").grid(row=1, column=1, padx=5, pady=5, sticky='w')
title_entry = tk.Entry(root, width=30)
title_entry.grid(row=2, column=1, padx=5, pady=0, sticky='ew')


tk.Label(root, text="저자:").grid(row=3, column=1, padx=5, pady=5, sticky='w')
author_entry = tk.Entry(root, width=30)
author_entry.grid(row=4, column=1, padx=5, pady=0, sticky='ew')


button_frame = tk.Frame(root)
button_frame.grid(row=5, column=1, pady=15) 

borrow_button = tk.Button(button_frame, text="대출", command=handle_borrow, width=10)
borrow_button.pack(side=tk.LEFT, padx=10)

return_button = tk.Button(button_frame, text="반납", command=handle_return, width=10)
return_button.pack(side=tk.LEFT, padx=10)


result_label = tk.Label(root, text="결과 메시지", justify=tk.CENTER)
result_label.grid(row=6, column=0, columnspan=3, padx=5, pady=10, sticky='n')


root.geometry("400x250") 
root.resizable(False, False)

root.mainloop()

