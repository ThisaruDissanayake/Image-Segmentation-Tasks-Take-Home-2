# Image Segmentation Tasks - Take Home 2 🧠🖼️
Welcome to a hands-on exploration of image segmentation techniques using Python!This repository demonstrates practical methods like Otsu Thresholding and Region Growing with noise robustness testing using Gaussian Noise.

## 🧪 Description

This project showcases simple but powerful segmentation approaches:

Synthetic image creation (or load your own)

Noise addition using Gaussian distribution

Otsu's Thresholding for automatic binarization

Region Growing from seed points for connected segment detection

The results are saved and displayed using OpenCV, NumPy, and Matplotlib.

## 📁 Directory Structure

<pre>Image-Segmentation-Tasks-Take-Home-2/
│
├── main.py                 # Main Python script for running all tasks
├── original_image.png      # Original synthetic image
├── noisy_image.png         # Image with Gaussian noise
├── otsu_result.png         # Result after Otsu's thresholding
├── region_grown.png        # Result after Region Growing
├── test1.png               # Optional input image
├── test.jpg                # Optional input image
├── EG_2020_3912_TakeHome_2.pdf  # Provided assignment
└── README.md               # You are here!</pre>

## 🛠️ Features

✅ Synthetic Image Generation (circle + square)

✅ Add Gaussian Noise (adjustable std dev)

✅ Otsu Thresholding with Gaussian blur preprocessing

✅ Region Growing using seed-based connectivity and intensity difference

✅ Save all output results as .png files

## How to Run
1. Clone the Repository
   <pre>git clone https://github.com/ThisaruDissanayake/Image-Segmentation-Tasks-Take-Home-2.git
cd Image-Segmentation-Tasks-Take-Home-2</pre>

2. Install Required Libraries
   <pre>pip install opencv-python numpy matplotlib</pre>
3. Run the Script
   <pre>python main.py</pre>
   
📌 Result Analysis

1.Original Image:

The image contains two clear objects a gray circle and a white square placed on a black 
background. These represent two distinct pixel intensity levels (gray = 85, white = 170), 
along with the background (black = 0)

2.With Gaussian Noise:

Gaussian noise was added to simulate a real-world scenario where the image is not perfectly 
clean. As seen in the image, the objects now appear with random intensity variations, 
especially around their boundaries. However, their general shapes are still visible.

3.Otsu Threshold:

Otsu’s algorithm automatically calculated the optimal threshold to separate the objects from 
the background. In the output, the square is detected quite accurately, but the noisy circle 
appears broken and patchy. This shows that Otsu’s method can be affected by noise, 
especially on objects with lower intensity contrast (like the gray circle).

4.Region Grown:

Starting from a seed inside the circle, the region-growing algorithm successfully segmented 
the entire circular object. It did this by checking neighboring pixels with similar intensity 
values. This method was very effective even in the presence of noise, as it focused on local 
pixel similarity rather than a global threshold.
