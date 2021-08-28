#worse than covid
from PIL import Image
import random

weed = Image.open('weed_leaf.png')

def show_random():

    for i in range(100):
        weed.show()

show_random()