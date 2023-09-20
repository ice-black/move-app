import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Create the main tkinter window
root = tk.Tk()
root.title("Display Web Image in tkinter")

# Create a frame to hold the image
image_frame = tk.Frame(root)
image_frame.pack()

# Define the URL of the web image
image_url = "https://example.com/path/to/your/image.jpg"  # Replace with the actual image URL

# Download the image from the web
response = requests.get(image_url)
image_data = response.content

# Create a PIL Image object from the image data
image = Image.open(BytesIO(image_data))

# Create a PhotoImage object from the PIL Image
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(image_frame, image=photo)
image_label.pack()

# Keep a reference to the PhotoImage to prevent it from being garbage collected
image_label.photo = photo

# Start the tkinter main loop
root.mainloop()
