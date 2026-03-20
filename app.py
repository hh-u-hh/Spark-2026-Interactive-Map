import tkinter as tk

# Initialize map window
root = tk.Tk()
root.title("ECU Interactive Map")
root.configure(background="purple")

# Set window to full screen and allow exit with Esc key
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

# Get actual screen size
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

# Display title
tk.Label(root, text="ECU Interactive Map").pack()

# Create canvas and load map image
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

imagetest = tk.PhotoImage(file="assets/Map.png")
canvas.create_image(0, 0, anchor="nw", image=imagetest)

# Function to place buttons at specific coordinates
def place_button(canvas, text, x, y, anchor="center"):
    btn = tk.Button(canvas, text=text)
    canvas.create_window(x, y, anchor=anchor, window=btn)
    return btn

W = window_width
H = window_height

place_button(canvas, "Top Left", x=50, y=50)
place_button(canvas, "Top Center", x=W//2, y=50)
place_button(canvas, "Top Right", x=W-50, y=50)
place_button(canvas, "Middle Left", x=50, y=H//2)
place_button(canvas, "Center", x=W//2, y=H//2)
place_button(canvas, "Middle Right", x=W-50, y=H//2)
place_button(canvas, "Bottom Left", x=50, y=H-50)
place_button(canvas, "Bottom Center", x=W//2, y=H-50)
place_button(canvas, "Bottom Right", x=W-50, y=H-50)

root.mainloop()