import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image/cell_frame004148_x0126_y0201_red.jpg', cv2.IMREAD_GRAYSCALE)
height, width = image.shape

start_point = (0, height // 2)
end_point = (width - 1, height // 2)

line_color = 255  # White color
line_thickness = 1
image_with_line = cv2.line(image.copy(), start_point, end_point, line_color, line_thickness)

line_points = np.linspace(start_point[0], end_point[0], num=width, dtype=int)
line_pixel_values = [image[start_point[1], x] for x in line_points]

plt.imshow(image_with_line, cmap='gray', vmin=0, vmax=255)
plt.title('Image with Line')
plt.axis('off')
plt.show()

plt.figure(figsize=(6, 4))
plt.plot(line_pixel_values)
plt.xlabel('Pixel Position')
plt.ylabel('Pixel Value')
plt.title('Pixel Values along the Line')
plt.show()
