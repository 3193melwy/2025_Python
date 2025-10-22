import subprocess, sys; subprocess.run([sys.executable, '-m', 'ensurepip', '--upgrade']); subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip']); subprocess.run([sys.executable, '-m', 'pip', 'install', 'matplotlib'])

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 나머지 코드 작성


def plot_graph():
    x = float(x_entry.get())
    y = float(y_entry.get())
    x_data.append(x)
    y_data.append(y)
    ax.clear()
    ax.plot(x_data, y_data, marker = 'o', linestyle= '-')
    canvas.draw()

# --- 애플리케이션 초기 설정 ---
root = tk.Tk()
root.title("Dynamic Line Graph")

x_data = []  # x좌표 데이터 저장할 리스트
y_data = []  # y좌표 데이터 저장할 리스트

x_label = tk.Label(root, text="Enter x coordinate:")  # x좌표 라벨
x_label.pack()
x_entry = tk.Entry(root)  # x좌표 입력창
x_entry.pack()

y_label = tk.Label(root, text="Enter y coordinate:")  # y좌표 라벨
y_label.pack()
y_entry = tk.Entry(root)  # y좌표 입력창
y_entry.pack()

# --- 그래프 그리는 함수 ---
def plot_graph():
    try:
        x = float(x_entry.get())
        y = float(y_entry.get())
        x_data.append(x)
        y_data.append(y)

        ax.clear()
        ax.plot(x_data, y_data, marker='o')
        canvas.draw()
    except ValueError:
        print("숫자를 입력하세요.")

plot_button = tk.Button(root, text="Plot", command=plot_graph)  # Plot 버튼
plot_button.pack()

# --- Matplotlib Figure 생성 ---
fig = Figure(figsize=(5, 4), dpi=100)  # 해상도 지정
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)  # 캔버스를 Tkinter에 연결
canvas.get_tk_widget().pack()

# --- 애플리케이션 실행 ---
root.mainloop()
