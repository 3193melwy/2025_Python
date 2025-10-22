import subprocess, sys; subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
import tkinter as tk
from PIL import ImageTk, Image
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def update_image():
    global current_index

    image_path = os.path.join(BASE_DIR, image_files[current_index])

    image = Image.open(image_path)

    image = image.resize((400,300))

    photo = ImageTk.PhotoImage(image)

    image_label.config(image=photo)
    image_label.image = photo

    current_index = (current_index +1) % len(image_files)
    root.after(interval, update_image)

root = tk.Tk()
root.title("Image Slider")

image_files = ["luke1.png","luke2.png","luke3.png","luke4.png"]

interval = 2000
current_index = 0

image_label = tk.Label(root)
image_label.pack()

update_image()

root.mainloop()



