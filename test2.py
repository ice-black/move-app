import tkinter as tk

def on_entry_click(widget, event):
    if widget.get() == "Placeholder Text":
        widget.delete(0, tk.END)
        widget.config(fg='black')  # Change text color to black

def on_focusout(widget, event):
    if not widget.get():
        widget.insert(0, "Placeholder Text")
        widget.config(fg='gray')  # Change text color to gray

root = tk.Tk()
root.geometry("300x200")

placeholder_text = "Placeholder Text"

entry = tk.Entry(root, fg='gray')  # Set the initial text color to gray
entry.insert(0, placeholder_text)
entry.bind("<FocusIn>", lambda e:  on_entry_click(entry))
entry.bind("<FocusOut>", lambda : on_focusout(entry))
entry.pack()

root.mainloop()
