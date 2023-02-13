from PIL import Image
img = Image.open('abc.jpg')
width, height = img.size
print(width, height)
img.show()  
