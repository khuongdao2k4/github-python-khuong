# VD 7 bài tình tổng 
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit # type: ignore

class SumApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Tính Tổng Hai Số")
        self.setGeometry(100, 100, 300, 200)

        self.label1 = QLabel("Nhập số thứ nhất:")
        self.num1 = QLineEdit(self)

        self.label2 = QLabel("Nhập số thứ hai:")
        self.num2 = QLineEdit(self)

        self.result_label = QLabel("Kết quả: ")
        self.button = QPushButton("Tính tổng")
        self.button.clicked.connect(self.calculate_sum)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.num1)
        layout.addWidget(self.label2)
        layout.addWidget(self.num2)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_sum(self):
        try:
            a = float(self.num1.text())
            b = float(self.num2.text())
            result = a + b
            self.result_label.setText(f"Kết quả: {result}")
        except ValueError:
            self.result_label.setText("Vui lòng nhập số hợp lệ!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SumApp()
    window.show()
    sys.exit(app.exec_prefix()) 
    
    # Ví dụ 1: Cửa sổ đầu tiên 
   
# Ví dụ 1: Cửa sổ đầu tiên
from tkinter import *

window = Tk()
window.title("Welcome to EAUT")
window.geometry("350x200")

window.mainloop()

# Ví dụ 2: Hiển thị Label
from tkinter import *

window = Tk()
window.title("Welcome to VniTeach app")

lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

window.mainloop()

# Ví dụ 3: Label và Button
from tkinter import *

window = Tk()
window.title("Welcome to EAUT")
window.geometry("350x200")

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

btn = Button(window, text="Click Me", bg="orange", fg="red")
btn.grid(column=1, row=0)

window.mainloop()

# Ví dụ 4: Xử lý sự kiện khi nhấn Button
from tkinter import *

window = Tk()
window.title("Welcome to EAUT")
window.geometry("350x200")

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

def clicked():
    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)

window.mainloop()

# Ví dụ 5: Hiển thị MessageBox
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")

def helloCallBack():
    messagebox.showinfo("Hello Python", "Hello World")

B = Button(top, text="Hello", command=helloCallBack)
B.place(x=50, y=50)

top.mainloop()

# Ví dụ 6: Textbox và Button
from tkinter import *

window = Tk()
window.title("Welcome to EAUT")
window.geometry('350x200')

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.focus()

def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()

# Ví dụ 7: Combobox (Danh sách lựa chọn)
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Welcome to EAUT")
window.geometry('350x200')

combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Text")
combo.current(1)  # Set giá trị mặc định
combo.grid(column=0, row=0)

window.mainloop()

# Ví dụ 8: Checkbox
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Welcome EAUT")
window.geometry('350x200')

chk_state = BooleanVar()
chk_state.set(True)  # Checkbox mặc định được chọn

chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=0)

window.mainloop()

# Ví dụ 9: Radio Button
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Welcome to EAUT")

selected = IntVar()

rad1 = Radiobutton(window, text='First', value=1, variable=selected)
rad2 = Radiobutton(window, text='Second', value=2, variable=selected)
rad3 = Radiobutton(window, text='Third', value=3, variable=selected)

def clicked():
    print(selected.get())

btn = Button(window, text="Click Me", command=clicked)

rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
btn.grid(column=3, row=0)

window.mainloop()

# Ví dụ 10: Hộp thoại chọn File và Thư mục
from tkinter import filedialog
from os import path

file = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
dir = filedialog.askdirectory()

file_with_initial_dir = filedialog.askopenfilename(initialdir=path.dirname(__file__)) 


    


    

    

    
