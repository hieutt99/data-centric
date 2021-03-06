import os, sys 

from utils.datasets import create_dataloader

CUR_DIR = os.getcwd()
BASE_DIR = os.path.dirname(CUR_DIR)
DATA_DIR = os.path.join(BASE_DIR, 'dataset')
MODE = 'train'
IMAGE_DIR = os.path.join(DATA_DIR, 'images', MODE)
LABEL_DIR = os.path.join(DATA_DIR, 'labels', MODE)


# files = os.listdir(IMAGE_DIR)

# print(len(files))

from temp import LoadImagesAndLabels

dataset = LoadImagesAndLabels(DATA_DIR, augment=True)

for item in dataset:
    print(item.size())

# for batch in loader:
#     print(batch)
