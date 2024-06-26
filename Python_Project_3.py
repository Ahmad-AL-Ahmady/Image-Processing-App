import cv2
import numpy as np
from customtkinter import *
from PIL import Image, ImageTk
from CTkMessagebox import CTkMessagebox

set_appearance_mode("dark")
set_default_color_theme("dark-blue")


class ImageProcessing:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Processing App")
        self.frame = CTkFrame(master)
        self.frame.pack(padx=10, pady=10)
        self.image_label = CTkLabel(self.frame,
                                    width=320,
                                    height=320)
        self.image_label.pack(padx=10, pady=10)
        self.load_image_button = CTkButton(
            master=self.master, text="Load Image", command=self.load_default_image)
        self.load_image_button.pack(pady=6)

        # Create IntVar for slider value
        self.erosion_kernel_size_var = IntVar(value=5)
        self.dilation_kernel_size_var = IntVar(value=5)
        self.open_kernel_size_var = IntVar(value=5)
        self.close_kernel_size_var = IntVar(value=5)
        self.add_buttons_and_sliders()

    def load_default_image(self):
        path = "assets/baboon.png"
        self.original_image = cv2.imread(path)
        self.update_image(self.original_image)

    def update_image(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        self.image_label.configure(image=img, text="")
        self.image_label.pack()

    def add_button(self, text, command):
        button = CTkButton(
            master=self.master, text=text, command=command, width=200)
        button.pack(pady=6)

    def add_buttons_and_sliders(self):
        # Erosion:
        self.erosion_slider_label = CTkLabel(self.master,
                                             text=f"Erosion Kernel Size: {self.erosion_kernel_size_var.get()}")
        self.erosion_slider_label.pack()

        self.erosion_slider = CTkSlider(
            self.master,
            from_=1,
            to=20,
            command=self.update_erosion_slider_label,
            variable=self.erosion_kernel_size_var,
            orientation=HORIZONTAL,
        )
        self.erosion_slider.set(5)
        self.erosion_slider.pack()
        self.add_button(text="Apply Erosion", command=self.apply_erosion)

        # Dilation:
        self.dilation_slider_label = CTkLabel(self.master,
                                              text=f"Dilation Kernel Size: {self.dilation_kernel_size_var.get()}")
        self.dilation_slider_label.pack()

        self.dilation_slider = CTkSlider(
            self.master,
            from_=1,
            to=20,
            command=self.update_dilation_slider_label,
            variable=self.dilation_kernel_size_var,
            orientation=HORIZONTAL,
        )
        self.dilation_slider.set(5)
        self.dilation_slider.pack()
        self.add_button(text="Apply Dilation", command=self.apply_dilation)

        # Open:
        self.open_slider_label = CTkLabel(self.master,
                                          text=f"Open Kernel Size: {self.open_kernel_size_var.get()}")
        self.open_slider_label.pack()

        self.open_slider = CTkSlider(
            self.master,
            from_=1,
            to=20,
            command=self.update_open_slider_label,
            variable=self.open_kernel_size_var,
            orientation=HORIZONTAL,
        )
        self.open_slider.set(5)
        self.open_slider.pack()
        self.add_button(text="Apply Open", command=self.apply_open)

        # Close:
        self.close_slider_label = CTkLabel(self.master,
                                           text=f"Close Kernel Size: {self.close_kernel_size_var.get()}")
        self.close_slider_label.pack()

        self.close_slider = CTkSlider(
            self.master,
            from_=1,
            to=20,
            command=self.update_close_slider_label,
            variable=self.close_kernel_size_var,
            orientation=HORIZONTAL,
        )
        self.close_slider.set(5)
        self.close_slider.pack()
        self.add_button(text="Apply Close", command=self.apply_close)

    def update_erosion_slider_label(self, event):
        self.erosion_slider_label.configure(
            text=f"Erosion Kernel Size: {self.erosion_kernel_size_var.get()}")

    def update_dilation_slider_label(self, event):
        self.dilation_slider_label.configure(
            text=f"Dilation Kernel Size: {self.dilation_kernel_size_var.get()}")

    def update_open_slider_label(self, event):
        self.open_slider_label.configure(
            text=f"Open Kernel Size: {self.open_kernel_size_var.get()}")

    def update_close_slider_label(self, event):
        self.close_slider_label.configure(
            text=f"Close Kernel Size: {self.close_kernel_size_var.get()}")

    def apply_erosion(self):
        kernel_size = int(self.erosion_kernel_size_var.get())
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        erosion_image = cv2.erode(self.original_image, kernel, iterations=1)
        self.update_image(erosion_image)

    def apply_dilation(self):
        kernel_size = int(self.dilation_kernel_size_var.get())
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        dilation_image = cv2.dilate(self.original_image, kernel, iterations=1)
        self.update_image(dilation_image)

    def apply_open(self):
        kernel_size = int(self.open_kernel_size_var.get())
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        open_image = cv2.morphologyEx(
            self.original_image, cv2.MORPH_OPEN, kernel)
        self.update_image(open_image)

    def apply_close(self):
        kernel_size = int(self.close_kernel_size_var.get())
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        close_image = cv2.morphologyEx(
            self.original_image, cv2.MORPH_CLOSE, kernel)
        self.update_image(close_image)


root = CTk()
root.geometry("400x750")
root.resizable(width=False, height=False)
root.title("Image Processing App")
APP = ImageProcessing(root)
root.mainloop()
