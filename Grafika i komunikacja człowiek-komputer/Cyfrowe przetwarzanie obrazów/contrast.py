from PIL import Image

def adjust_contrast(image, contrast):
    resultImage = Image.new("RGB", (image.width, image.height))

    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            adjusted_pixel = [0, 0, 0]

            for i in range(3):
                v = pixel[i]

                if contrast >= 0:
                    adjusted_pixel[i] = int((127 / (127 - contrast)) * (v - contrast))
                else:
                    adjusted_pixel[i] = int(((127 + contrast) / 127) * (v - contrast))

                adjusted_pixel[i] = max(0, min(255, adjusted_pixel[i]))

            resultImage.putpixel((x, y), tuple(adjusted_pixel))

    resultImage.show()

image = Image.open("Images/flower3.png")

adjust_contrast(image, -50)