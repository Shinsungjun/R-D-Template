import torch
from torch.utils import data
import glob
from PIL import Image

class CustomDataset(data.Dataset):
    def __init__(self, split = 'train'):
        super().__init__()
        #!path 만 저장 하고 나중에 getitem에서 그걸 참고해서
        #!진짜 이미지 or 정답지를 불러온다
        self.data_root = "/src/mydataset/"
        self.files = glob.glob(self.data_root+ split + "*.png")

    def __len__(self):
        return len(self.files)


    def __getitem__(self, index):
        data_path = self.files[index]
        img = Image.open(data_path)
        label_path = data_path.replace("train", "label")
        label = Image.open(label_path)
        #! transform (augmentation)
        img, label = transform(img, label)
        return img, label
