import threading
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
import io ,time
import base64


def imagen_2(image_path, screen_width, screen_height, widget): # image processing
    def load_image():
        try:
            image = Image.open(image_path)
        except Exception as e:
            try:
                image = Image.open(io.BytesIO(image_path))
            except Exception as e:
                print(e)
                binary_data = base64.b64decode(image_path)  # Decode the string
                image = Image.open(io.BytesIO(binary_data))

        image = image.resize((screen_width, screen_height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        widget.config(image=photo)
        widget.image = photo  # Keep a reference to the PhotoImage to prevent it from being garbage collected

    image_thread = threading.Thread(target=load_image)  # Create a thread to load the image asynchronously
    image_thread.start()


C = tk.Tk()

screenwidth = C.winfo_screenwidth()
screenheight = C.winfo_screenheight()
start_w = 600
start_h = 400
C.minsize(start_w, start_h)
C.maxsize(start_w, start_h)
pos_w = int((screenwidth / 2) - (start_w / 2))
pos_h = int((screenheight / 2) - (start_h / 2))
C.geometry(f'+{pos_w}+{pos_h}')
m = tk.Label(C)
m.pack(fill='both', expand=True)


image = Image.open("Assets/startup.jpg")
image = image.resize((pos_w, pos_h), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
m.config(image=photo)

#C.overrideredirect(True)
C.config(bg='blue')


def close_stratup():
    C.destroy()


m.after(5000, close_stratup)


#C.protocol("WM_DELETE_WINDOW", on_closing)
C.mainloop()
print('end')