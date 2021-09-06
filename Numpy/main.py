import numpy
import cv2

def p(x):
    print(x)

num = numpy.arange(27)
p(num)

num2 = num.reshape(3, 3, 3)
p(num2)

#cheese = numpy.asarray([[123, 12, 123, 12, 33], [], []])
#p(type(cheese))

img = cv2.imread("smallgray.png", 0)
p(img)

cv2.imwrite("newsmallgray.png", img)

#p(img[3, 4])

p("*"*160)

for i in img:
    print(i)

p("*"*160)

for i in img.flat:
    print(i)


ims = numpy.hstack((img, img))

p(ims)

lst = numpy.hsplit(ims, 3)
p(lst)