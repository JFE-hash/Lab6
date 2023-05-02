from PIL import Image

water_name = 'eft.png'
with Image.open(water_name) as water_img:
    water_img.load()

file = '1.jpg'
with Image.open(file) as img:
    img.load()

img.paste(water_img, (100, 1450), water_img)
img.show()
img.save('img_with_water.jpg')