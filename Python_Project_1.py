import cv2
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
        self.hpf_kernel_size_var = IntVar(value=5)
        self.mean_kernel_size_var = IntVar(value=5)
        self.median_kernel_size_var = IntVar(value=5)
        self.roberts_kernel_size_var = IntVar(value=5)
        self.add_buttons_and_sliders()

    def load_default_image(self):
        path = "assets/lenna.png"
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
        # HPF:
        self.hpf_slider_label = CTkLabel(self.master,
                                         text=f"HPF Kernel Size: {self.hpf_kernel_size_var.get()}")
        self.hpf_slider_label.pack()

        self.hpf_slider = CTkSlider(
            self.master,
            from_=1,
            to=20,
            command=self.update_hpf_slider_label,  # Update label on slider change
            variable=self.hpf_kernel_size_var,
            orientation=HORIZONTAL,
        )
        self.hpf_slider.set(5)
        self.hpf_slider.pack()
        self.add_button(text="Apply HPF", command=self.apply_hpf)

        # MEAN:
        self.mean_slider_label = CTkLabel(self.master,
                                          text=f"Mean Kernel Size: {self.hpf_kernel_size_var.get()}")
        self.mean_slider_label.pack()

        self.mean_slider = CTkSlider(
            self.master,
            from_=1,
            to=20,
            command=self.update_mean_slider_label,  # Update label on slider change
            variable=self.mean_kernel_size_var,
            orientation=HORIZONTAL,
        )
        self.mean_slider.set(5)
        self.mean_slider.pack()
        self.add_button(text="Apply Mean", command=self.apply_mean)

        # Median:
        self.median_slider_label = CTkLabel(self.master,
                                            text=f"Median Kernel Size: {self.median_kernel_size_var.get()}")
        self.median_slider_label.pack()

        self.median_slider = CTkSlider(
            self.master,
            from_=1,
            to=20,
            command=self.update_median_slider_label,  # Update label on slider change
            variable=self.median_kernel_size_var,
            orientation=HORIZONTAL,
        )
        self.median_slider.set(5)
        self.median_slider.pack()
        self.add_button(text="Apply Median", command=self.apply_median)

    def update_hpf_slider_label(self, event):
        self.hpf_slider_label.configure(
            text=f"HPF Kernel Size: {self.hpf_kernel_size_var.get()}")

    def update_mean_slider_label(self, event):
        self.mean_slider_label.configure(
            text=f"Mean Kernel Size: {self.mean_kernel_size_var.get()}")

    def update_median_slider_label(self, event):
        self.median_slider_label.configure(
            text=f"Median Kernel Size: {self.median_kernel_size_var.get()}")

    def apply_hpf(self):
        kernel_size = int(self.hpf_kernel_size_var.get())
        if (kernel_size % 2 == 0):
            CTkMessagebox(title="Warning Message!", message="Kernel size must be odd.",
                          icon="warning", option_1="Ok")
        else:
            # Apply HPF using the kernel size
            gray_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
            blurred_image = cv2.GaussianBlur(
                gray_image, (kernel_size, kernel_size), 0)
            hpf_image = cv2.subtract(gray_image, blurred_image)
            self.update_image(cv2.cvtColor(hpf_image, cv2.COLOR_GRAY2BGR))

    def apply_mean(self):
        kernel_size = int(self.mean_kernel_size_var.get())
        mean_image = cv2.blur(self.original_image, (kernel_size, kernel_size))
        self.update_image(mean_image)

    def apply_median(self):
        kernel_size = int(self.median_kernel_size_var.get())
        if (kernel_size % 2 == 0):
            CTkMessagebox(title="Warning Message!", message="Kernel size must be odd.",
                          icon="warning", option_1="Ok")
        else:
            median_image = cv2.medianBlur(self.original_image, kernel_size)
            self.update_image(median_image)


root = CTk()
root.geometry("400x650")
root.resizable(width=False, height=False)
root.title("Image Processing App")
APP = ImageProcessing(root)
root.mainloop()
