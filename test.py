import struct
from PIL import Image
from PIL import ImageDraw

f = open("font.bin", "rb")

space_width, line_spacing, num_chars = struct.unpack("cch", f.read(4))

space_width = ord(space_width)
line_spacing = ord(line_spacing)

print("SPACE_WIDTH: {}".format(space_width))
print("LINE_SPACING: {}".format(line_spacing))
print("NUM_CHARS: {}".format(num_chars))

for charnum in range(num_chars):
    num_rects, width = struct.unpack("cc", f.read(2))
    num_rects = ord(num_rects)
    width = ord(width)

    print("\tNUM_RECTS: {}".format(num_rects))
    print("\tWIDTH: {}".format(width))
    img = Image.new("RGB", (width+1, 9 + 1))
    imgd = ImageDraw.Draw(img)
    for rectnum in range(num_rects):
        x, y, width, height = struct.unpack("cccc", f.read(4))
        x = ord(x)
        y = ord(y)
        width = ord(width)
        height = ord(height)

        print("\t\tX: {}".format(x))
        print("\t\tY: {}".format(y))
        print("\t\tWIDTH: {}".format(width))
        print("\t\tHEIGHT: {}".format(height))

        imgd.line(((x, y), (x + width-1, y + height-1)))

    img.save("{}.png".format(str(charnum).zfill(3)))
