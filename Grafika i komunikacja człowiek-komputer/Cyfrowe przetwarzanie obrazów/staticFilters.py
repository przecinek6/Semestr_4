from PIL import Image

def min_filter(image, size):
    width, height = image.size
    filtered_image = Image.new("RGB", (width, height))

    half_size = int(size) // 2

    for x in range(width):
        for y in range(height):
            min_r = min_g = min_b = 255
            for i in range(-half_size, half_size + 1):
                for j in range(-half_size, half_size + 1):
                    nx, ny = x + i, y + j
                    if 0 <= nx < width and 0 <= ny < height:
                        pixel = image.getpixel((nx, ny))
                        min_r = min(min_r, pixel[0])
                        min_g = min(min_g, pixel[1])
                        min_b = min(min_b, pixel[2])

            filtered_image.putpixel((x, y), (min_r, min_g, min_b))

    return filtered_image

def max_filter(image, size):
    width, height = image.size
    filtered_image = Image.new("RGB", (width, height))

    half_size = int(size) // 2

    for x in range(width):
        for y in range(height):
            max_r = max_g = max_b = 0
            for i in range(-half_size, half_size + 1):
                for j in range(-half_size, half_size + 1):
                    nx, ny = x + i, y + j
                    if 0 <= nx < width and 0 <= ny < height:
                        pixel = image.getpixel((nx, ny))
                        max_r = max(max_r, pixel[0])
                        max_g = max(max_g, pixel[1])
                        max_b = max(max_b, pixel[2])

            filtered_image.putpixel((x, y), (max_r, max_g, max_b))

    return filtered_image

def median_filter(image, size):
    from statistics import median

    width, height = image.size
    filtered_image = Image.new("RGB", (width, height))

    half_size = int(size) // 2

    for x in range(width):
        for y in range(height):
            pixels = []
            for i in range(-half_size, half_size + 1):
                for j in range(-half_size, half_size + 1):
                    nx, ny = x + i, y + j
                    if 0 <= nx < width and 0 <= ny < height:
                        pixel = image.getpixel((nx, ny))
                        pixels.append(pixel)

            median_r = median([p[0] for p in pixels])
            median_g = median([p[1] for p in pixels])
            median_b = median([p[2] for p in pixels])

            filtered_image.putpixel((x, y), (int(median_r), int(median_g), int(median_b)))

    return filtered_image