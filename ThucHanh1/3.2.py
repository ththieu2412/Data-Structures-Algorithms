import cv2

import matplotlib.pyplot as plt

# Read the image
cat_image = cv2.imread("ThucHanh1/binary_cat.png", 0)

# Display the image
cv2.imshow("Cat Image", cat_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


counts = dict()
height, width = cat_image.shape
for row in range(height):
  for col in range(width):
      counts[cat_image[row,col]] = counts.get(cat_image[row,col],0) + 1

print('Counts', counts)

names = list(counts.keys())
values = list(counts.values())

plt.bar(range(len(counts)), values, tick_label=names)
plt.show()