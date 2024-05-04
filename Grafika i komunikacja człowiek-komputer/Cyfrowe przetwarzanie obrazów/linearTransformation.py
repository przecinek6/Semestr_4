from PIL import Image

def rozjasnienie(image, percent):
    resultImage = Image.new("RGB", (image.width, image.height))

    w, h = image.size

    for i in range(w):
        for j in range(h):
            r, g, b = image.getpixel((i, j))
            r = max(0, min(255, r * ((percent / 100) + 1)))
            g = max(0, min(255, g * ((percent / 100) + 1)))
            b = max(0, min(255, b * ((percent / 100) + 1)))
            resultImage.putpixel((i, j), (int(r), int(g), int(b)))

    resultImage.save("rozjasnienie.jpg")

def przyciemnienie(image, percent):
    resultImage = Image.new("RGB", (image.width, image.height))

    w, h = image.size

    for i in range(w):
        for j in range(h):
            r, g, b = image.getpixel((i, j))
            r = max(0, min(255, r * (1 - (percent / 100))))
            g = max(0, min(255, g * (1 - (percent / 100))))
            b = max(0, min(255, b * (1 - (percent / 100))))
            resultImage.putpixel((i, j), (int(r), int(g), int(b)))

    resultImage.save("przyciemnienie.jpg")

def negatyw(image):
    resultImage = Image.new("RGB", (image.width, image.height))

    w, h = image.size

    for i in range(w):
        for j in range(h):
            r, g, b = image.getpixel((i, j))
            r = 255 - r
            g = 255 - g
            b = 255 - b
            resultImage.putpixel((i, j), (r, g, b))

    resultImage.save("negatyw.jpg")

image = Image.open("bialystok.jpg")

negatyw(image)
rozjasnienie(image, 100)
przyciemnienie(image, 70)