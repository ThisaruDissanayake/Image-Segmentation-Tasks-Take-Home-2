import cv2
import numpy as np
import matplotlib.pyplot as plt

# IMAGE SOURCE SELECTION 
def load_image(use_local=False, local_path='test.jpg'):
    if use_local:
        image = cv2.imread(local_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise FileNotFoundError(f"Image not found at: {local_path}")
        return image
    else:
        image = np.zeros((100, 100), dtype=np.uint8)
        cv2.circle(image, (30, 30), 15, 85, -1)
        cv2.rectangle(image, (60, 60), (85, 85), 170, -1)
        return image

#  ADD GAUSSIAN NOISE 
def add_gaussian_noise(image, mean=0, std=50):
    noise = np.random.normal(mean, std, image.shape).astype(np.int16)
    noisy_img = np.clip(image.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    return noisy_img

#  OTSU'S THRESHOLDING 
def apply_otsu(image):
    blur = cv2.GaussianBlur(image, (5, 5), 0)
    
    otsu_val, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    print(f"Otsu's threshold value: {otsu_val}")
    return thresh

#  REGION GROWING 
def region_growing(image, seeds, threshold=10):
    visited = np.zeros_like(image, dtype=bool)
    output = np.zeros_like(image, dtype=np.uint8)
    h, w = image.shape
    seed_value = image[seeds[0][1], seeds[0][0]]
    stack = list(seeds)

    while stack:
        x, y = stack.pop()
        if visited[y, x]:
            continue
        visited[y, x] = True
        current_val = image[y, x]
        if abs(int(current_val) - int(seed_value)) <= threshold:
            output[y, x] = 255
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < w and 0 <= ny < h and not visited[ny, nx]:
                    stack.append((nx, ny))
    return output

# Toggle between synthetic and local image
use_local_image = False  # Set to True to load your own image
local_image_path = 'D:/7 Semester/computer vision/Take Home 2/test1.png' 

image = load_image(use_local=use_local_image, local_path=local_image_path)
noisy_image = add_gaussian_noise(image)
otsu_result = apply_otsu(noisy_image)
seed_points = [(30, 30)] if not use_local_image else [(70, 70)]  # adjust seed 
region_result = region_growing(image, seed_points, threshold=20)

cv2.imwrite("original_image.png", image)
cv2.imwrite("noisy_image.png", noisy_image)
cv2.imwrite("otsu_result.png", otsu_result)
cv2.imwrite("region_grown.png", region_result)

plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1), plt.imshow(image, cmap='gray'), plt.title("Original")
plt.subplot(2, 2, 2), plt.imshow(noisy_image, cmap='gray'), plt.title("With Gaussian Noise")
plt.subplot(2, 2, 3), plt.imshow(otsu_result, cmap='gray'), plt.title("Otsu Threshold")
plt.subplot(2, 2, 4), plt.imshow(region_result, cmap='gray'), plt.title("Region Grown")
plt.tight_layout()
plt.show()
