from PIL import Image

def resizeImage(image1, image2):
    width = min(image1.width, image2.width)
    height = min(image1.height, image2.height)
    return image1.resize((width, height)), image2.resize((width, height))

def additiveMode(image1, image2):
    resultImage = Image.new("RGB", (image1.width, image1.height))

    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            blended_pixel = [0, 0, 0]
            for i in range(3):
                p1, p2 = pixel1[i], pixel2[i]
                blended_pixel[i] = min(p1 + p2, 255)

            resultImage.putpixel((x, y), tuple(blended_pixel))

    resultImage.show()

def subtractiveMode(image1, image2):
    resultImage = Image.new("RGB", (image1.width, image1.height))

    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            blended_pixel = [0, 0, 0]
            for i in range(3):
                p1, p2 = pixel1[i], pixel2[i]
                blended_pixel[i] = max(0, p1 - p2)

            resultImage.putpixel((x, y), tuple(blended_pixel))

    resultImage.show()

def differenceMode(image1, image2):
    resultImage = Image.new("RGB", (image1.width, image1.height))

    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            blended_pixel = [0, 0, 0]
            for i in range(3):
                p1, p2 = pixel1[i], pixel2[i]
                blended_pixel[i] = max(0, abs(p1 - p2))

            resultImage.putpixel((x, y), tuple(blended_pixel))

    resultImage.show()

def multiplyMode(image1, image2):
    resultImage = Image.new("RGB", (image1.width, image1.height))

    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            blended_pixel = [0, 0, 0]
            for i in range(3):
                p1, p2 = pixel1[i], pixel2[i]
                blended_pixel[i] = ((p1 * p2) // 255)

            resultImage.putpixel((x, y), tuple(blended_pixel))

    resultImage.show()

def screenMode(image1, image2):
    resultImage = Image.new("RGB", (image1.width, image1.height))

    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            blended_pixel = [0, 0, 0]
            for i in range(3):
                p1, p2 = pixel1[i], pixel2[i]
                blended_pixel[i] = 255 - (((255 - p1) * (255 - p2)) // 255)

            resultImage.putpixel((x, y), tuple(blended_pixel))

    resultImage.show()

def negationMode(image1, image2):
    resultImage = Image.new("RGB", (image1.width, image1.height))

    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            blended_pixel = [0, 0, 0]
            for i in range(3):
                p1, p2 = pixel1[i], pixel2[i]
                blended_pixel[i] = 255 - abs(255 - p1 - p2)

            resultImage.putpixel((x, y), tuple(blended_pixel))

    resultImage.show()

def darkenMode(image1, image2):
    resultImage = Image.new("RGB", (image1.width, image1.height))

    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            blended_pixel = [0, 0, 0]
            for i in range(3):
                p1, p2 = pixel1[i], pixel2[i]
                if p1 < p2:
                    blended_pixel[i] = p1
                else:
                    blended_pixel[i] = p2

            resultImage.putpixel((x, y), tuple(blended_pixel))

    resultImage.show()

def lightenMode(image1, image2):
    resultImage = Image.new("RGB", (image1.width, image1.height))

    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            blended_pixel = [0, 0, 0]
            for i in range(3):
                p1, p2 = pixel1[i], pixel2[i]
                if p1 > p2:
                    blended_pixel[i] = p1
                else:
                    blended_pixel[i] = p2

            resultImage.putpixel((x, y), tuple(blended_pixel))

    resultImage.show()

def exclusionMode(image1, image2):
    resultImage = Image.new("RGB", (image1.width, image1.height))

    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            blended_pixel = [0, 0, 0]
            for i in range(3):
                p1, p2 = pixel1[i], pixel2[i]
                blended_pixel[i] = p1 + p2 - (2 * p1 * p2) // 255

            resultImage.putpixel((x, y), tuple(blended_pixel))

    resultImage.show()

def overlayMode(image1, image2):
    resultImage = Image.new("RGB", (image1.width, image1.height))

    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            blended_pixel = [0, 0, 0]
            for i in range(3):
                p1, p2 = pixel1[i], pixel2[i]
                if p1 < 128:
                    blended_pixel[i] = 2 * p1 * p2 // 255
                else:
                    blended_pixel[i] = 255 - 2 * (255 - p1) * (255 - p2) // 255

            resultImage.putpixel((x, y), tuple(blended_pixel))

    resultImage.show()

def hardLightMode(image1, image2):
    resultImage = Image.new("RGB", (image1.width, image1.height))

    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            blended_pixel = [0, 0, 0]
            for i in range(3):
                p1, p2 = pixel1[i], pixel2[i]
                if p2 < 128:
                    blended_pixel[i] = 2 * p1 * p2 // 255
                else:
                    blended_pixel[i] = 255 - 2 * (255 - p1) * (255 - p2) // 255

            resultImage.putpixel((x, y), tuple(blended_pixel))

    resultImage.show()

def softLightMode(image1, image2):
    resultImage = Image.new("RGB", (image1.width, image1.height))

    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            blended_pixel = [0, 0, 0]
            for i in range(3):
                p1 = pixel1[i] / 255.0
                p2 = pixel2[i] / 255.0

                if p2 < 0.5:
                    blended_pixel[i] = 2 * p1 * p2 + p1 * p1 * (1 - 2 * p2)
                else:
                    blended_pixel[i] = p1 ** 0.5 * (2 * p2 - 1) + (2 * p1) * (1 - p2)

                blended_pixel[i] *= 255
                blended_pixel[i] = max(0, min(255, int(blended_pixel[i])))

            resultImage.putpixel((x, y), tuple(blended_pixel))

    resultImage.show()

def colorDodgeMode(image1, image2):
    resultImage = Image.new("RGB", (image1.width, image1.height))

    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            blended_pixel = [0, 0, 0]
            for i in range(3):
                p1 = pixel1[i] / 255.0
                p2 = pixel2[i] / 255.0

                blended_pixel[i] = p1 / (1 - p2)

                blended_pixel[i] *= 255
                blended_pixel[i] = max(0, min(255, int(blended_pixel[i])))

            resultImage.putpixel((x, y), tuple(blended_pixel))

    resultImage.show()

def colorBurnMode(image1, image2):
    resultImage = Image.new("RGB", (image1.width, image1.height))

    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            blended_pixel = [0, 0, 0]
            for i in range(3):
                p1 = pixel1[i] / 255.0
                p2 = pixel2[i] / 255.0

                if p2 != 0:
                    blended_pixel[i] = 1 - (1 - p1) / p2
                else:
                    blended_pixel[i] = 0

                blended_pixel[i] *= 255
                blended_pixel[i] = max(0, min(255, int(blended_pixel[i])))

            resultImage.putpixel((x, y), tuple(blended_pixel))

    resultImage.show()

def reflectMode(image1, image2):
    resultImage = Image.new("RGB", (image1.width, image1.height))

    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            blended_pixel = [0, 0, 0]
            for i in range(3):
                p1 = pixel1[i] / 255.0
                p2 = pixel2[i] / 255.0

                blended_pixel[i] = p1 ** 2 / (1 - p2)

                blended_pixel[i] *= 255
                blended_pixel[i] = max(0, min(255, int(blended_pixel[i])))

            resultImage.putpixel((x, y), tuple(blended_pixel))

    resultImage.show()

def transparency(image1, image2, alpha):
    resultImage = Image.new("RGB", (image1.width, image1.height))

    for x in range(image1.width):
        for y in range(image1.height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            blended_pixel = [0, 0, 0]
            for i in range(3):
                blended_pixel[i] = int((1 - alpha) * pixel2[i] + alpha * pixel1[i])

            resultImage.putpixel((x, y), tuple(blended_pixel))

    resultImage.show()

image1 = Image.open("Images/flower1.png")
image2 = Image.open("Images/flower2.png")

image1, image2 = resizeImage(image1, image2)

# additiveMode(image1, image2)
# subtractiveMode(image1, image2)
# differenceMode(image1, image2)
# multiplyMode(image1, image2)
# screenMode(image1, image2)
# negationMode(image1, image2)
# darkenMode(image1, image2)
# lightenMode(image1, image2)
# exclusionMode(image1, image2)
# overlayMode(image1, image2)
# hardLightMode(image1, image2)
# softLightMode(image1, image2)
# colorDodgeMode(image1, image2)
# colorBurnMode(image1, image2)
# reflectMode(image1, image2)
transparency(image1, image2, 0.1)