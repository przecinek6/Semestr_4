from PIL import Image

def potegowa(image, gamma):
    resultImage = Image.new("RGB", (image.width, image.height))

    w, h = image.size

    for i in range(w):
        for j in range(h):
            r, g, b = image.getpixel((i, j))
            r = int((r / 255.0) ** gamma * 255)
            g = int((g / 255.0) ** gamma * 255)
            b = int((b / 255.0) ** gamma * 255)
            resultImage.putpixel((i, j), (r, g, b))

    resultImage.save("resultPotegowa.jpg")


image = Image.open("bialystok.jpg")

potegowa(image, 0.5)