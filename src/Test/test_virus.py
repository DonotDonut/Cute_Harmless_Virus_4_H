import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import threading

def show_cute_animation():
    root = tk.Tk()
    root.title("Happy Bunny Virus 🐰")
    root.geometry("500x550") # width, x height
    root.configure(bg='pink') # background color 
    root.resizable(False, False) # parameters: width & height

    # Create a frame to organize layout vertically
    main_frame = tk.Frame(root, bg='white')
    main_frame.pack(fill='both', expand=True)

    # Label for GIF/message
    # boarder of the gifs 
    lbl = tk.Label(main_frame, bg='blue')
    lbl.pack(expand=True)

    # Frame for buttons
    btn_frame = tk.Frame(main_frame, bg='red') #background color
    btn_frame.pack(pady=10)

    # buttons 
    def on_yes():
        show_message()
        print("You clicked YES!")

    def on_no():
        print("You clicked NO!")

    tk.Button(btn_frame, text="Yes", command=on_yes, font=("Arial", 12), bg='white').pack(side='left', padx=10)
    tk.Button(btn_frame, text="No", command=on_no, font=("Arial", 12), bg='white').pack(side='right', padx=10)

    # Load and animate GIF
    gif = Image.open('media/Cat Working GIF.gif')
    frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(gif)]

    def animate(counter=0):
        lbl.configure(image=frames[counter])
        root.after(100, animate, (counter + 1) % len(frames))

    animate()

    def show_message():
        def update_ui():
            lbl.config(
                image='',
                text="You've been visited by the 🐰 Happy Bunny Virus!\nHave a wonderful day!",
                font=("Arial", 16),
                justify="center"
            )
        root.after(0, update_ui)
        

    threading.Thread(target=lambda: (threading.Event().wait(5), show_message()), daemon=True).start()

    root.mainloop()

# Run method 
show_cute_animation()
