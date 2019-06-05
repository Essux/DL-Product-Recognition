from PIL import Image, ImageOps
import time
import os
from tqdm import tqdm
rootdir = './dataset'

iters = 0
N = 200
for subdir, dirs, files in tqdm(list(os.walk(rootdir))):
    for file in files:
        #if iters>10: break
        #print(os.path.join(subdir, file))
        if not file.endswith('.jpg') and not file.endswith('.JPG'): continue
        original_image = Image.open(os.path.join(subdir, file))
        size = (N, N)
        new_image = ImageOps.fit(original_image, size, Image.ANTIALIAS)
        subfolder_name = os.path.basename(subdir)

        new_folder = os.path.join('./processed/', subfolder_name)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        new_image.save(os.path.join('./processed/', subfolder_name, file))
        iters += 1
