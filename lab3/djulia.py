from PIL import Image

w, h, zoom = 192 * 5, 108 * 5, 1

image = Image.new("RGB", (w, h), "white")

cX, cY = -0.7, 0.27015
moveX, moveY = 0.0, 0.0
maxIter = 255

for x in range(w):
    for y in range(h):
        zx = 1.5 * (x - w / 2) / (0.5 * zoom * w) + moveX
        zy = 1.0 * (y - h / 2) / (0.5 * zoom * h) + moveY
        i = maxIter
        while zx * zx + zy * zy < 4 and i > 1:
            tmp = zx * zx - zy * zy + cX
            zy, zx = 2.0 * zx * zy + cY, tmp
            i -= 1
        image.putpixel((x, y), (i % 16, i % 32, i % 16))

image.show()


