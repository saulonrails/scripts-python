from PIL import Image
img = Image.open("")
print(img.size)
print(img.format)
print(img.mode)
img.show()
