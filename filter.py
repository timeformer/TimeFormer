from glob import glob
from tqdm import tqdm
import os

imgs = sorted(glob('compare_rgb/*/*/*.png'))

valid_imgs = open('valid.txt', 'r').readlines()

valid_imgs = [valid_img.replace('\n', '') for valid_img in valid_imgs]

print(valid_imgs)

for img in tqdm(imgs):
    if img not in valid_imgs:
        os.system(f'rm {img}')


