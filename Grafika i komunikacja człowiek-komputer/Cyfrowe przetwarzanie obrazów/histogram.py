import numpy as np
import matplotlib.pyplot as plt

def generate_histogram(image):
    img_array = np.array(image)

    r_channel = img_array[:, :, 0].flatten()
    g_channel = img_array[:, :, 1].flatten()
    b_channel = img_array[:, :, 2].flatten()

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.hist(r_channel, bins=256, color='red', alpha=0.7)
    plt.title('Red Channel')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')

    plt.subplot(1, 3, 2)
    plt.hist(g_channel, bins=256, color='green', alpha=0.7)
    plt.title('Green Channel')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')

    plt.subplot(1, 3, 3)
    plt.hist(b_channel, bins=256, color='blue', alpha=0.7)
    plt.title('Blue Channel')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()