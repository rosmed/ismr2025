import numpy as np
import matplotlib.pyplot as plt

images = np.load("path_to_images-file_with_ultrasound")
segmentations = np.load("path_to_labels-file_with_segmentation")

for i in range(segmentations.shape[0]):
    if np.any(segmentations[i] == 1):
        image_slice = images[i, :, :, 0]
        seg_slice = segmentations[i, :, :, 0]

        # Display side-by-side
        plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)
        plt.imshow(image_slice, cmap='gray')
        plt.title(f'Image Index {i}')
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.imshow(seg_slice, cmap='gray')
        plt.title('Segmentation')
        plt.axis('off')

        plt.tight_layout()
        plt.show()


