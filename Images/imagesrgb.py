from PIL import Image

red = Image.open('red.png')
blue = Image.open('blue.png')

blue.show()

blue.paste(im=red, box=(0,0), mask=red)

blue.show()
blue.save("purple.png")

