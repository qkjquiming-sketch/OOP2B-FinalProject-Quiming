from PIL import Image

img = Image.open("customIcon.png").convert("RGBA")

# pad to square so it doesn't get stretched
size = max(img.size)
square = Image.new("RGBA", (size, size), (0, 0, 0, 0))
square.paste(img, ((size - img.width) // 2, (size - img.height) // 2))
square = square.resize((256, 256), Image.LANCZOS)

square.save("icon.png")
square.save("icon.ico", sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
print("Done: icon.png and icon.ico")