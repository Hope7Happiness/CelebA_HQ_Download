import os
# import PIL
from PIL import Image

import numpy as np
import hashlib

# celeba_dir = './celeba-1024'
# celeba_dir = os.path.join(os.path.dirname(__file__), 'celeba-1024')


# img = np.array(Image.open(os.path.join(celeba_dir, '000004.jpg')))
# md5 = hashlib.md5()
# md5.update(img.tobytes())

# print('md5 sum:', md5.hexdigest())

# dir2 = '/dataset/CelebA_HQ_docker/celebA/img_celeba.7z.004'
dir2 = '/dataset/CelebA_HQ_docker/celebA-HQ/deltas07000.zip'

print(hashlib.sha1(open(dir2, 'rb').read()).hexdigest())
