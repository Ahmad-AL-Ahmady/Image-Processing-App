import cv2
import numpy as np
from customtkinter import *
from PIL import Image, ImageTk
from CTkMessagebox import CTkMessagebox

set_appearance_mode("dark")
set_default_color_theme("darkblue")


class ImageProcessing:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Processing App")
        self.frame = CTkFrame(master)
        self.frame.pack(padx=10, pady=10)

        self.image_label = CTkLabel(self.frame)
        self.image_label.pack(padx=10, pady=10)

        self.load_image_button = CTkButton(
            master=self.master, text="Load Image", command=self.load_default_image
        )
        self.load_image_button.pack()

        # Create IntVar for slider value
        self.kernel_size_var = IntVar(value=5)
        self.add_buttons_and_sliders()

    def load_default_image(self):
        path = "lenna.png"
        self.original_image = cv2.imread(path)
        self.update_image(self.original_image)

    def update_image(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        self.image_label.configure(image=img, text="")
        self.image_label.pack()

    def add_buttons_and_sliders(self):
        self.slider_label = CTkLabel(self.master,
                                     text=f"HPF Kernel Size: {self.kernel_size_var.get()}")
        self.slider_label.pack()

        self.slider = CTkSlider(
            self.master,
            from_=1,
            to=20,
            command=self.update_slider_label,  # Update label on slider change
            variable=self.kernel_size_var,
            orientation=HORIZONTAL,
        )
        self.slider.set(5)
        self.slider.pack()

        hpf_button = CTkButton(
            master=self.master, text="Apply HPF", command=self.apply_hpf)
        hpf_button.pack(pady=6)

    def update_slider_label(self, event):
        # Update slider label to show current value
        self.slider_label.configure(
            text=f"Kernel Size: {self.kernel_size_var.get()}")

    def apply_hpf(self):
        kernel_size = int(self.kernel_size_var.get())  # Get value from IntVar
        if (kernel_size % 2 == 0):
            CTkMessagebox(title="Warning Message!", message="Kernel size must be odd in HPF.",
                          icon="warning", option_1="Ok")

        else:
            # Apply HPF using the kernel size
            gray_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
            blurred_image = cv2.GaussianBlur(
                gray_image, (kernel_size, kernel_size), 0)
            hpf_image = cv2.subtract(gray_image, blurred_image)
            self.update_image(cv2.cvtColor(hpf_image, cv2.COLOR_GRAY2BGR))


root = CTk()
root.geometry("800x600")
root.title("Image Processing App")
APP = ImageProcessing(root)
root.mainloop()
