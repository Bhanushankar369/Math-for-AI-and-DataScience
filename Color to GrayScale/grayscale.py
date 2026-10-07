import cv2
import numpy as np

img = cv2.imread('22A31A05J6.jpeg')

# for i in range(len(img)):
#     print()
#     print(img[i])
    
b_vector = img[:, :, 0]
g_vector = img[:, :, 1]
r_vector = img[:, :, 2]

print(b_vector.shape)

height = img.shape[0]
width = img.shape[1]

gray_vector = np.zeros((height, width), dtype = np.uint8)
gray_image = np.zeros((height, width), dtype = np.uint8)

print(gray_vector.shape)

for i in range(1280):
    for j in range(963):
        gray_image[i][j] = (b_vector[i][j] + r_vector[i][j] + g_vector[i][j]) / 3
        
gray_vector[:, :] = (0.50 * r_vector) + (0.30 * g_vector) + (0.20 * b_vector)

import numpy as np
gray_image = np.array(gray_image, dtype=np.uint8)
        
cv2.imwrite('output_img_with_values3.jpeg', gray_vector)
cv2.imwrite('output_gray.jpg', gray_image)