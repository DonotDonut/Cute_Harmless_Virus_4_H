import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import threading
import time

def show_cute_animation():
    root = tk.Tk()
    root.title("Happy Bunny Virus 🐰")
    root.geometry("500x500")
    root.configure(bg='pink')
    root.resizable(False, False)

    # Load animated GIF
    gif = Image.open('Test/Cat Working GIF.gif')  # Add your own animated GIF here
    lbl = tk.Label(root, bg='pink')
    lbl.pack(expand=True)

    frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(gif)]

    def animate(counter=0):
        lbl.configure(image=frames[counter])
        root.after(100, animate, (counter + 1) % len(frames))

    animate()

    # Display message after delay
    def show_message():
        time.sleep(5)
        lbl.config(image='', text="You've been visited by the 🐰 Happy Bunny Virus!\nHave a wonderful day!", font=("Arial", 16), justify="center")

    threading.Thread(target=show_message, daemon=True).start()

    root.mainloop()



show_cute_animation()
