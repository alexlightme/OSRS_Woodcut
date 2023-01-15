import matplotlib.pyplot as plt

def show_images(image):
    plt.figure(figsize=(18,18))
    plt.imshow(image)
    plt.axis('off')
    plt.show()
