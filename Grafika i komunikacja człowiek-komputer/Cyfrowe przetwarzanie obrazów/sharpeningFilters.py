from PIL import Image

def filterFunction(image, filter):
    width, height = image.size
    filtered_image = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            sum_r = sum_g = sum_b = 0

            for i in range(-1, 2):
                for j in range(-1, 2):
                    nx, ny = x + i, y + j
                    if 0 <= nx < width and 0 <= ny < height:
                        pixel = image.getpixel((nx, ny))
                    else:
                        nx = max(0, min(nx, width - 1))
                        ny = max(0, min(ny, height - 1))
                        pixel = image.getpixel((nx, ny))

                    filter_value = filter[i + 1][j + 1]
                    sum_r += pixel[0] * filter_value
                    sum_g += pixel[1] * filter_value
                    sum_b += pixel[2] * filter_value

            new_r = min(max(int(sum_r), 0), 255)
            new_g = min(max(int(sum_g), 0), 255)
            new_b = min(max(int(sum_b), 0), 255)

            filtered_image.putpixel((x, y), (new_r, new_g, new_b))
    filtered_image.show()


image = Image.open("Images/filters.png")

robertsHorizontal = [[0, 0, 0], [0, 1, -1], [0, 0, 0]]
robertsVertical = [[0, 0, 0], [0, 1, 0], [0, -1, 0]]

prewittHorizontal = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]
prewittVertical = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]

sobelHorizontal = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
sobelVertical = [[1, 0, -1], [2, 0, -2],[1, 0, -1]]

laplace = [[-1, -1, -1], [-1, 8, -1],[-1, -1, -1]]


# filterFunction(image, robertssHorizontal)
# filterFunction(image, robertsVertical)
# filterFunction(image, prewittHorizontal)
# filterFunction(image, prewittVertical)
# filterFunction(image, sobelHorizontal)
# filterFunction(image, sobelVertical)
filterFunction(image, laplace)
