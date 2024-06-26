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
        self.add_buttons_and_sliders()

    def load_default_image(self):
        path = "assets/cameraman.png"
        self.original_image = cv2.imread(path)
        self.update_image(self.original_image)

    def update_image(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        self.image_label.configure(image=img, text="")
        self.image_label.pack()

    def add_buttons_and_sliders(self):
        # Roberts:
        self.add_button("Apply Roberts Edge Detector", self.apply_roberts)

        # Prewitt:
        self.add_button("Apply Prewitt Edge Detector", self.apply_prewitt)

        # Solbel:
        self.add_button("Apply Solbel Edge Detector", self.apply_solbel)

        # Hough Circle
        self.add_button("Apply Hough Circle Transform",
                        self.apply_hough_circle)

        # Disclaimer:
        disclaimer = CTkLabel(
            master=self.master,
            width=200,
            text_color="grey",
            text="Prewitt and Solbel Edge Dtetctors may have the same effect \non the photo as they are similar in their underlying principles \nand often produce comparable results, especially when \napplied to images with similar characteristics.",)
        disclaimer.pack(pady=6, padx=10)

    def add_button(self, text, command):
        button = CTkButton(
            master=self.master, text=text, command=command, width=200)
        button.pack(pady=6)

    def apply_roberts(self):
        roberts_image = cv2.Canny(self.original_image, 100, 200)
        self.update_image(roberts_image)

    def apply_prewitt(self):
        gray_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        prewitt_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
        prewitt_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
        prewitt_image = np.sqrt(prewitt_x**2 + prewitt_y**2)
        prewitt_image = cv2.normalize(
            prewitt_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        self.update_image(prewitt_image)

    def apply_solbel(self):
        gray_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
        sobel_image = np.sqrt(sobel_x**2 + sobel_y**2)
        sobel_image = cv2.normalize(
            sobel_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        self.update_image(sobel_image)

    def apply_hough_circle(self):
        gray_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(gray_image, cv2.HOUGH_GRADIENT, dp=1,
                                   minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            hough_image = self.original_image.copy()
            for i in circles[0, :]:
                cv2.circle(hough_image, (i[0], i[1]), i[2], (0, 255, 0), 2)
                cv2.circle(hough_image, (i[0], i[1]), 2, (0, 0, 255), 3)
            self.update_image(hough_image)


root = CTk()
root.geometry("400x650")
root.resizable(width=False, height=False)
root.title("Image Processing App")
APP = ImageProcessing(root)
root.mainloop()
