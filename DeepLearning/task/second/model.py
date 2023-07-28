import torch
from torchvision import datasets, transforms, models
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
import matplotlib.pyplot as plt
import torch.nn.functional as F
import torch.optim as optim

class VGG16(nn.Module):
    def __init__(self):
        super(VGG16, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(128, 128, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2,stride=2),
            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(256, 512, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.avgpool = nn.AdaptiveAvgPool2d(1)
        self.classifier = nn.Sequential(
            nn.Linear(512, 256),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(256, 128),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = x.reshape(x.shape[0], -1)
        x = self.classifier(x)

        return x

class ResNet(nn.Module):
    def __init__(self):
        super(ResNet, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, padding=1),
            nn.ReLU(inplace=True)
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64)
        )
        self.conv3 = nn.Sequential(
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64)
        )
        self.conv4 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.Conv2d(128, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128)    
        )
        self.conv5 = nn.Sequential(
            nn.Conv2d(128, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.Conv2d(128, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128)    
        )
        self.conv6 = nn.Sequential(
            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256)    
        )
        self.conv7 = nn.Sequential(
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256)    
        )
        self.conv8 = nn.Sequential(
            nn.Conv2d(256, 512, kernel_size=3, padding=1),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.BatchNorm2d(512)    
        )
        self.conv9 = nn.Sequential(
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.BatchNorm2d(512)
        )
        self.avgpool = nn.AdaptiveAvgPool2d(1)
        self.fc10 = nn.Sequential(
            nn.Linear(512, 256),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(256, 128),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(128, 10)
        )
        self.conv1x1_1 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=1, padding=0),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.conv1x1_2 = nn.Sequential(
            nn.Conv2d(128, 256, kernel_size=1, padding=0),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.conv1x1_3 = nn.Sequential(
            nn.Conv2d(256, 512,kernel_size=1, padding=0),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        

    def forward(self, x):
        x1 = self.conv1(x)

        x2 = self.conv2(x1)
        x2 = F.relu(x2 + x1)

        x3 = self.conv3(x2)
        x3 = F.relu(x3 + x2)

        x4 = self.conv4(x3)
        x3 = self.conv1x1_1(x3)
        x4 = F.relu(x4 + x3)

        x5 = self.conv5(x4)
        x5 = F.relu(x5 + x4)

        x6 = self.conv6(x5)
        x5 = self.conv1x1_2(x5)
        x6 = F.relu(x6 + x5)

        x7 = self.conv7(x6)
        x7 = F.relu(x7 + x6)

        x8 = self.conv8(x7)
        x7 = self.conv1x1_3(x7)
        x8 = F.relu(x8 + x7)

        x9 = self.conv9(x8)
        x9 = F.relu(x9 + x8)

        out = self.avgpool(x9)
        out = out.reshape(out.shape[0], -1)
        out = self.fc10(out)

        return out
        
class AlexNet(nn.Module):
    def __init__(self):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 96, kernel_size=7, stride=2, padding=0),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2, padding=0),
            nn.Conv2d(96, 256, kernel_size=5, stride=1, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2, padding=0),
            nn.Conv2d(256, 384, kernel_size=3, stride=1, padding=1),
            nn.Conv2d(384, 384, kernel_size=3, stride=1, padding=1),
            nn.Conv2d(384, 256, kernel_size=3, stride=1, padding=1),
            nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        )
        self.avgpool = nn.AdaptiveAvgPool2d(1)
        self.classifier = nn.Sequential(
            nn.Linear(256, 128),
            nn.Dropout(),
            nn.ReLU(inplace=True),
            nn.Linear(128, 64),
            nn.Dropout(),
            nn.ReLU(inplace=True),
            nn.Linear(64, 10)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = x.reshape(x.shape[0], -1)
        x = self.classifier(x)

        return x



if __name__ == "__main__":
    net = AlexNet()

    print(net)