import torch
import torch.nn as nn
import torch.nn.functional as F

# 残差网络
class Residual(nn.Module):
    def __init__(self, in_channels, out_channels, stride=1):
        super(Residual, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.relu1 = nn.ReLU()
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(out_channels)

        if in_channels == out_channels:
            self.conv1x1 = None
        else:
            self.conv1x1 = nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride)
    
    def forward(self, x):
        x1 = self.relu1(self.bn1(self.conv1(x)))
        x1 = self.bn2(self.conv2(x1))

        if self.conv1x1:
            x = self.conv1x1(x)

        out = self.relu1(x1 + x)

        return out

# 网络模型
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(1, 10, kernel_size=5, stride=1, padding=2),
            Residual(10, 10),
            Residual(10, 10),
            Residual(10, 10)
        )
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Sequential(
            nn.Conv2d(10, 20, kernel_size=5, stride=1, padding=2),
            Residual(20, 20),
            Residual(20, 20),
            Residual(20, 20)
        )
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.fc1 = nn.Linear(7*7*20, 100)
        self.fc2 = nn.Linear(100, 50)
        self.fc3 = nn.Linear(50, 10)

    def forward(self, x):
        x = self.pool1(self.conv1(x))
        x = self.pool2(self.conv2(x))
        x = x.reshape(x.shape[0], -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)

        return x
    