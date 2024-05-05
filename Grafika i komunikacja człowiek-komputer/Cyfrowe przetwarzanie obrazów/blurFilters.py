from PIL import Image

def box_filter(image, size):
    width, height = image.size
    filtered_image = Image.new("RGB", (width, height))

    half_size = size // 2

    for x in range(width):
        for y in range(height):
            r_total = g_total = b_total = 0
            count = 0

            for i in range(max(0, x - half_size), min(width, x + half_size + 1)):
                for j in range(max(0, y - half_size), min(height, y + half_size + 1)):
                    pixel = image.getpixel((i, j))
                    r_total += pixel[0]
                    g_total += pixel[1]
                    b_total += pixel[2]
                    count += 1

            # Calculate the average value for each channel
            r_avg = r_total // count
            g_avg = g_total // count
            b_avg = b_total // count

            filtered_image.putpixel((x, y), (r_avg, g_avg, b_avg))

    filtered_image.show()

image = Image.open("Images/bialystok.jpg")

box_filter(image, 3)