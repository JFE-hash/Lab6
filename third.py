from PIL import Image, ImageFilter

names = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']

for file in names:
    with Image.open(file) as img:
        img.load()

        filt_img = img.filter(ImageFilter.EMBOSS)
        filt_img.show()
        filt_img.save('new_' + file)