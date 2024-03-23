from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2
import pytesseract
import messagebox



def load_default_image():
    global panelA

    # Specify the path to your default image
    default_image_path = "E:/pythonProject/car2.jpg"

    # Load the image using OpenCV and convert it to RGB
    image = cv2.imread("E:/pythonProject/car2.jpg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert the image to PIL format
    image_pil = Image.fromarray(image)

    # Convert the PIL image to Tkinter format
    image_tk = ImageTk.PhotoImage(image_pil)

    # If panelA is None, create a new Label widget with the default image
    if panelA is None:
        panelA = Label(frame1, image=image_tk)
        panelA.image = image_tk
        panelA.pack(side="left", padx=10, pady=10)
    else:
        # If panelA already exists, update its image
        panelA.configure(image=image_tk)
        panelA.image = image_tk

def detect_edges_and_extract_text():
    global panelB

    # Load the default image
    image = cv2.imread("E:/pythonProject/car2.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 100)

    # Convert the edges image to PIL format
    edges_pil = Image.fromarray(edges)

    # Extract text from edged image
    extracted_text = pytesseract.image_to_string(edges)

    # Display the extracted text in a messagebox
    messagebox.showinfo("Extracted Text", extracted_text)

    # Convert the PIL image to Tkinter format
    edges_tk = ImageTk.PhotoImage(edges_pil)

    if panelB is None:
        panelB = Label(frame2, image=edges_tk)
        panelB.image = edges_tk
        panelB.pack(side="left", padx=10, pady=10)
    else:
        panelB.configure(image=edges_tk)
        panelB.image = edges_tk


# Create the Tkinter window
root = Tk()

# Create global variables to store the image panel
panelA = None
panelB = None

# Create a frame to hold the default image
frame1 = Frame(root)
frame1.pack(side="top", padx=10, pady=10)

# Load the default image when the application starts
load_default_image(r"E:/pythonProject/car2.jpg")

# Create frames for displaying processed images
frame2 = Frame(root)
frame2.pack(side="top", padx=10, pady=10)

# Create buttons to trigger image processing functions
btn_detect_edges = Button(root, text="Detect Edges and Extract Text", command=detect_edges_and_extract_text)
btn_detect_edges.pack(side="left", padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
