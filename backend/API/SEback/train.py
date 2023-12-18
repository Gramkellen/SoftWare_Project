from torchvision.models import resnet18
import torch.nn as nn
import torch
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
import os
import glob
import numpy as np

model = resnet18(weights=True)  # 设为True加载预训练权重

channel_in = model.fc.in_features
model.fc = nn.Sequential(nn.Linear(channel_in,2))

from PIL import Image
lambda x: Image.open(x).convert('RGB') 

class Mydataset(Dataset):
    def __init__(self, root, resize):
        super(Mydataset, self).__init__()
        self.root = root
        self.resize = resize
        self.imgs = []
        self.labels = []

        # class_0
        path = os.path.join(self.root + "class_0/", "*.jpg")
#         print(path)
        imgs = glob.glob(path)
        for i in range(len(imgs)):
            self.imgs.append(imgs[i])
            self.labels.append(0)
            
        # class_1
        imgs = glob.glob(os.path.join(self.root + "class_1/", "*.jpg"))
        for i in range(len(imgs)):
            self.imgs.append(imgs[i])
            self.labels.append(1)
        

    def __len__(self):
        return len(self.imgs)

    def __getitem__(self, idx): 
        print(len(self.imgs))
        img, label = self.imgs[idx], self.labels[idx]
        tf = transforms.Compose([
            lambda x: Image.open(x).convert('RGB'),
            transforms.Resize((int(self.resize), int(self.resize))),
            # transforms.Resize((int(self.resize * 1.25), int(self.resize * 1.25))),
            # transforms.RandomRotation(15),
            # transforms.CenterCrop(self.resize),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
        ])

        img = tf(img)
        label = torch.tensor(label)
        return img, label


#模型参数处理：
#定义损失函数
import torch.nn as nn
criterion = nn.CrossEntropyLoss() 
#定义优化器
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
#数据集划分
from torch.utils.data import DataLoader, random_split

dataset = Mydataset(r"/root/traindata/data/", 224)
train_ratio = 0.8
batch_size = 10
n_train = int(train_ratio * len(dataset))
n_val = len(dataset) - n_train
print("data number: {}, train: {}, val: {}".format(len(dataset), n_train, n_val))
train_dataset, val_dataset = random_split(dataset, [n_train, n_val])

train_loader = DataLoader(train_dataset, batch_size, True)
val_loader = DataLoader(val_dataset, batch_size, False)


#训练模型
from torch.autograd import Variable

start_epoch = 0
epoch_num = 25
#device = 'cuda'
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model.to(device)
for epoch in range(start_epoch, epoch_num): 
        # train
        model.train()
        for i, (imgs, labels) in enumerate(train_loader): 
            inputs = Variable(imgs).to(device)
            labels = Variable(labels).to(device) 
            optimizer.zero_grad()
            outputs = model(inputs)  
            loss = criterion(outputs, labels)   
            loss.backward()
            optimizer.step()

            print('[ Train Epoch {:005d} -> {:005d} / {} ] loss : {:15} '.format(
                epoch, i, len(train_loader), loss.item()))

        # val
        model.eval()
        with torch.no_grad():
            val_loss = 0.0
            for i, (imgs, labels) in enumerate(val_loader):
                inputs = Variable(imgs).to(device)
                labels = Variable(labels).to(device) 
                 
                outputs = model(inputs)
               
                val_loss += criterion(outputs, labels).item()

            val_loss /= len(val_loader)
            print('******* val  loss : {:15} '.format(val_loss))

        if epoch == epoch_num - 1:
            torch.save(model.state_dict(), "./New-resnet18-2Class.pth")