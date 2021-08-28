from PIL import Image

weed = Image.open('weed_leaf.png')

weed.show()
print(weed.size)

halfway = 1920/2
x = halfway - 200
w = halfway + 200

y = 800
h = 1257

leaf = weed.crop((x, y, w, h))
leaf.show()

weed.paste(im=leaf, box=(796,300))

weed.show()

weed.rotate(180)
weed.show()


