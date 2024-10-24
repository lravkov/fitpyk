import tkinter as tk
from PIL import Image, ImageTk
import time


def fitpyk_display_image(image_path):
    # Create a Tkinter window
    root = tk.Tk()
    root.title("fitPyk")

    # Open the image file
    img = Image.open(image_path)

    # Convert the image to Tkinter format
    img_tk = ImageTk.PhotoImage(img)

    # Create a label with the image
    label = tk.Label(root, image=img_tk)
    label.pack()

    # Update the window
    root.update()

    # Wait for 1 second
    time.sleep(1)

    # Close the window
    root.destroy()


if __name__ == "__main__":
    # # Example usage:
    # image_path = "fitPyk.jpeg"
    # fitpyk_display_image(image_path)
    pass

