import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox

# Initialize map window
root = tk.Tk()
root.title("ECU Interactive Map")
root.configure(background="white")

# Set window to full screen and allow exit with Esc key
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

# Get actual screen size
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

# Create canvas filling the entire window (no label pushing things down)
canvas = tk.Canvas(root, width=window_width, height=window_height, highlightthickness=0, bg="white")
canvas.pack()

# Load and resize to fit the window while maintaining aspect ratio
pil_image = Image.open("assets/Map.png")
orig_width, orig_height = pil_image.size
scale = min(window_width / orig_width, window_height / orig_height)
new_width = int(orig_width * scale)
new_height = int(orig_height * scale)
pil_image = pil_image.resize((new_width, new_height), Image.LANCZOS)
imagetest = ImageTk.PhotoImage(pil_image)

btn_top_left = ImageTk.PhotoImage(Image.open("assets/studentCenter.png").resize((200, 200), Image.LANCZOS))
btn_top_center = ImageTk.PhotoImage(Image.open("assets/copula.png").resize((200, 150), Image.LANCZOS))
btn_middle_left = ImageTk.PhotoImage(Image.open("assets/library.png").resize((200, 150), Image.LANCZOS))
btn_center = ImageTk.PhotoImage(Image.open("assets/bateBuilding.png").resize((200, 150), Image.LANCZOS))
btn_middle_right = ImageTk.PhotoImage(Image.open("assets/fletcher.png").resize((200, 150), Image.LANCZOS))
btn_explore = ImageTk.PhotoImage(Image.open("assets/sciTech.png").resize((200, 150), Image.LANCZOS))

# Load character image for next to text box
character_image = ImageTk.PhotoImage(Image.open("assets/peeDee.png").resize((300, 300), Image.LANCZOS))


# Places image at the center of the canvas
canvas.create_image(window_width // 2, window_height // 2, anchor="center", image=imagetest)

# Function to handle button clicks
messages = {
    "Top Left": "ECU student center is the central hub of the university, most big events are hosted here. There are many opportunities for engagement, as well as lost of food. The adress is 501 East 10th Street.",
    "Top Center": "The cupola is the heart of campus. Legend says that if you walk under it, you wont graduate on time!!!",
    "Middle Left": "The library is a quiet place for those times when you need to focus. Whether you are studying for a test, writing a paper or just need a quiet place to read, the library is the place to be. It is located in 1000 E 5th St right next to the student center.",
    "Center": "Bate building is the place where several classes take place, whether you are into economics or gobal culture this is a place where you can cantiniously learn and grow. It is located next to sci tech in Founders Dr.",
    "Middle Right": "The fletcher building is a place where musicians can go at it. Its safe space to create, be yourself and meet other musicians. its near the brewster building in Ormond Wy.",
    "Explore": "This is SciTech. Where some of the engineering and science classes are held. There is innnovation and research happening all the time here, its a great place to explore if you like these subjects. You should be able to spot the location as soon as you turn in Founders Dr.",
}

def button_action(text):
    message = messages.get(text, f"You clicked the {text} button.")
    text_label.config(text=f"PeeDee: {message}")

# Function to place image buttons with transparent background
def place_button(canvas, text, x, y, image, anchor="center"):
    item = canvas.create_image(x, y, image=image, anchor=anchor)
    canvas.tag_bind(item, "<Button-1>", lambda e: button_action(text))
    canvas.tag_bind(item, "<Enter>", lambda e: canvas.config(cursor="hand2"))
    canvas.tag_bind(item, "<Leave>", lambda e: canvas.config(cursor=""))
    return item

W = window_width
H = window_height

place_button(canvas, "Top Left",      x=290,      y=375, image=btn_top_left)
place_button(canvas, "Top Center",    x=W-750,    y=300, image=btn_top_center)
place_button(canvas, "Middle Left",   x=565,      y=H-500, image=btn_middle_left)
place_button(canvas, "Center",        x=W//2,    y=H-350, image=btn_center)
place_button(canvas, "Middle Right",  x=W-370,    y=700, image=btn_middle_right)
place_button(canvas, "Explore",       x=W//2,    y=H-200, image=btn_explore)


# Text display for visual novel style messages
text_label = tk.Label(root, text="", anchor="w", font=("Arial", 16), bg="lightgray", fg="black", wraplength=window_width-500, relief="sunken", bd=5)
text_label.place(x=300, y=window_height-150, width=window_width-500, height=100)

# Character image next to text box (on canvas for transparent background)
canvas.create_image(150, window_height-150, image=character_image, anchor="center")

root.mainloop()