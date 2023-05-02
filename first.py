from PIL import Image

file = 'мама.jpg'

with Image.open(file) as img:
    img.load()

img.show()

width, height = img.size
typee = img.format
color_mode = img.mode

print(f'Разрешение изображения: {width}x{height}')
print('Формат изображения:', typee)
print('Цветовая модель изображения:', color_mode)