import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

import clr
from tkwebview2.tkwebview2 import WebView2, have_runtime, install_runtime
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Threading')
from System.Windows.Forms import Control
from System.Threading import Thread,ApartmentState,ThreadStart

if not have_runtime():  # 没有webview2 runtime
    install_runtime()
global hold
is_fullscreen = False



def main():
        global hold
        global is_fullscreen

        root = tk.Tk()
        root.title("Move App")
        root.state('zoomed') # this creates a window that takes over the screen
        root.minsize(150, 100)

        # Get the screen dimensions
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        large_frame_size = screen_height+700


        # Create a Canvas widget to hold the frame and enable scrolling
        canvas = tk.Canvas(root, highlightthickness=0)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a Scrollbar and connect it to the Canvas
        scrollbar = tk.Scrollbar(root, command=canvas.yview)
        #scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.config(yscrollcommand=scrollbar.set)

        # Create a frame to hold your content of the canvers
        frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor=tk.NW)

        # Create a large frame within the canvas frame (replace this with your content)
        large_frame = tk.Frame(frame, bg='gray', width=screen_width,  height=large_frame_size)
        large_frame.pack(fill=tk.X)

        def on_frame_configure(event):  # Update the canvas scrolling region when the large frame changes size
            canvas.configure(scrollregion=canvas.bbox("all"))

        def on_mouse_wheel(event):  # Function to handle mouse wheel scrolling
            # Scroll the canvas up or down based on the mouse wheel direction
            if event.delta < 0:
                canvas.yview_scroll(1, "units")
            else:
                canvas.yview_scroll(-1, "units")

        def Load_Movie(widget, movie_id):
            global hold
            movie_id = 'tt8385148'
            frame2 = WebView2(widget, 500, 5000)
            hold = frame2
            frame2.load_url(f'https://vidsrc.to/embed/movie/{movie_id}')
            frame2.pack(side='left', padx=0, fill='both', expand=True)

        def toggle_fullscreen(widget):
            global is_fullscreen
            if is_fullscreen:
                # Restore the video frame to its original size and position
                root.overrideredirect(False)
                widget.forget()
                widget.place(relx=0.03, rely=0.04, relheight=0.4, relwidth=0.94, x=original_x, y=original_y, width=original_width, height=original_height)
                is_fullscreen = False
            else:
                # Expand the video frame to full screen
                root.overrideredirect(True)
                widget.forget()
                widget.place(relx=0, rely=0, x=0, y=0, relwidth=1, relheight=screen_height/large_frame_size)
                is_fullscreen = True

        def imagen(widget):
            # Define the URL of the web image
            image_url = "https://m.media-amazon.com/images/M/MV5BMzI0NmVkMjEtYmY4MS00ZDMxLTlkZmEtMzU4MDQxYTMzMjU2XkEyXkFqcGdeQXVyMzQ0MzA0NTM@.jpg"  # Replace with the actual image URL

            # Download the image from the web
            response = requests.get(image_url)
            image_data = response.content

            # Create a PIL Image object from the image data
            image = Image.open(BytesIO(image_data))

            # Resize the image to match the frame's dimensions
            image = image.resize((screen_width, (screen_height)), Image.LANCZOS)

            # Create a PhotoImage object from the PIL Image
            photo = ImageTk.PhotoImage(image)
            return photo


        #  content:

        image_label = tk.Label(large_frame, bg='blue')
        image_label.place(relx=0, rely=0.0, relheight=0.45, relwidth=1)
        photo = imagen(image_label)
        image_label.config(image=photo)
        play_bn = tk.Button(image_label, text='▶' )
        play_bn.place(relx=0.49, rely=0.49, relheight=0.02, relwidth=0.02)


        video_box = tk.Frame(large_frame, bg='green')
        #video_box.place(relx=0.03, rely=0.04, relheight=0.4, relwidth=0.94)
        #Load_Movie(video_box, None)

        original_x = video_box.winfo_x()
        original_y = video_box.winfo_y()
        original_width = video_box.winfo_width()
        original_height = video_box.winfo_height()

        fullscreen_button = tk.Button(video_box, border=0, borderwidth=0, text="⤢",  bg='black', activebackground='black', activeforeground='white',fg='white', font = ('Arial Black', 26),  command=lambda: toggle_fullscreen(video_box))
        fullscreen_button.place(relx=0.97, rely=0.95, relheight=0.05, relwidth=0.03)

        label2 = tk.Button(large_frame, bg='green',text="This is a label in the large frame", command=lambda:hold.full_screeen())
        label2.place(x = 0.1, rely=0.7, relheight = 0.1)



        frame.bind("<Configure>", on_frame_configure)










        canvas.bind_all("<MouseWheel>", on_mouse_wheel)  # Bind the mouse wheel event to the canvas

        # Configure the canvas scrolling region to hide scrollbars
        canvas.configure(scrollregion=canvas.bbox("all"))




        root.mainloop()

if __name__ == "__main__":
    t = Thread(ThreadStart(main))
    t.ApartmentState = ApartmentState.STA
    t.Start()
    t.Join()