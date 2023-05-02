from PIL import Image

file = 'мама.jpg'

with Image.open(file) as img:
    img.load()

img_reduced = img.reduce(3)
img_reduced.save('урезанная мама.jpg')

img_flipped = img.rotate(180)
img_flipped.save('мама перевернулась.jpg')

img_hor_mirr = img.transpose(Image.FLIP_LEFT_RIGHT)
img_hor_mirr.save('мама горизонтально отразилась.jpg')

img_vert_mirr = img.transpose(Image.FLIP_LEFT_RIGHT)
img_vert_mirr.save('мама вертикально отразилась.jpg')