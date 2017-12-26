# -*- coding: utf-8 -*-
from PIL import Image
from random import shuffle
import argparse


class Shredder:

    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--path', help='absolute/relative path to the image file')
        args = parser.parse_args()
        return args

    def shred(self,args):
        image_path = args.path
        SHREDS = 250
        image = Image.open(image_path)
        # shredded = Image.new("1", image.size)
        width, height = image.size
        shred_width = width // SHREDS
        size = shred_width * SHREDS
        shredded = Image.new("RGB", (size, height))
        sequence = list(range(0, SHREDS))
        shuffle(sequence)
        for i, shred_index in enumerate(sequence):
            shred_x1, shred_y1 = shred_width * shred_index, 0
            shred_x2, shred_y2 = shred_x1 + shred_width, height
            region = image.crop((shred_x1, shred_y1, shred_x2, shred_y2))
            shredded.paste(region, (shred_width * i, 0))
            shredded.save(image_path)


if __name__ == '__main__':
    shredder = Shredder();
    args = shredder.get_args();
    sequence = shredder.shred(args);
