# Image Processing App

## Description
This is a simple image-processing application built using Python and CustomTkinter. It allows users to load an image and apply various image processing filters such as high-pass, mean, erosion, dilation, open, close, and median filters. As well as some edge detectors like Solbel, Prewitt, and Roberts edge detectors.

## Features
- Load image: Users can load an image from their local storage.
- Apply filters: Users can apply high-pass, mean, and median filters to the loaded image.
- Real-time preview: The application provides a real-time preview of the filtered image within the GUI.

## Installation
1. Clone the repository:
  git clone https://github.com/yAhmad-AL-Ahmady/image-processing-app.git
2. Install dependencies:
  pip install opencv-python numpy Pillow
3. Run the application:
  python image_processing_app.py

## Usage
1. Launch the application by running the script.
2. Click on the "Load Image" button to select an image from your local storage.
3. Adjust the slider for the desired kernel size of the filter.
4. Click on the respective "Apply" button to apply the filter (HPF, Mean, Median).
5. View the filtered image in real-time within the application.

## Dependencies
- OpenCV (cv2): For image processing operations.
- NumPy: For numerical computations.
- Pillow (PIL): For image handling and display.
- customtkinter: Custom library for Tkinter widgets.
- CTkMessagebox: Custom message box for Tkinter.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or create a pull request.
