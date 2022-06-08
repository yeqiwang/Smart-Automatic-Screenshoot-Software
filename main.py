from PIL import ImageGrab
from time import sleep
import numpy as np
import datetime
import os
from skimage.metrics import structural_similarity

def isSimiliary(pic1, pic2, threshold):
    pic1 = np.array(pic1)
    pic2 = np.array(pic2)

    temp = structural_similarity(pic1, pic2, multichannel=True)

    if temp < threshold:
        return False
    else:
        return True


if __name__ == '__main__':
    save_dir = './pic/'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    count = 0

    last_picture = ImageGrab.grab(all_screens=False)
    while(True):
        pic = ImageGrab.grab(all_screens=False)
        if not isSimiliary(last_picture, pic, 0.93):
            count += 1
            print('save the {}th picture.'.format(count))
            pic.save(save_dir + '{}.png'.format(datetime.datetime.now().strftime('%Y_%m%d_%H%M_%S')))
        last_picture = pic
        sleep(1)
