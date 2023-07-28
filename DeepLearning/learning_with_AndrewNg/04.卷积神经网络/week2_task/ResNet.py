import h5py
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt
import torch.nn as nn


class Image_Data(Dataset):
    def __init__(self, data_path):
        super(Image_Data, self).__init__()
        dataset = h5py.File(data_path, 'r')
        if data_path == 'DeepLearning/learning_with_AndrewNg/04.卷积神经网络/week2_task/datasets/train_signs.h5':
            data_set_x_orig = np.array(dataset['train_set_x'][:])
            data_set_y_orig = np.array(dataset['train_set_y'][:])
        elif data_path == 'DeepLearning/learning_with_AndrewNg/04.卷积神经网络/week2_task/datasets/test_signs.h5':
            data_set_x_orig = np.array(dataset['test_set_x'][:])
            data_set_y_orig = np.array(dataset['test_set_y'][:])
        
        data_set_x_orig = data_set_x_orig.astype('float32') / 255
        data_set_y_orig = data_set_y_orig.astype('float32')

        self.x_data = torch.from_numpy(data_set_x_orig)
        self.y_data = torch.from_numpy(data_set_y_orig)

        self.len = self.y_data.shape[0]

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    
    def __len__(self):
        return self.len
    
    def get_shape(self):
        return self.x_data.shape, self.y_data.shape
    
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
    
class ResNet(nn.Module):
    def __init__(self, in_channels, num_classes):
        super(ResNet, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(in_channels, 64, kernel_size=7, stride=2, padding=3),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True)
        )

        self.conv2 = nn.Sequential(
            nn.MaxPool2d(kernel_size=3, stride=2, padding=1),
            Residual(64, 64),
            Residual(64, 64),
            Residual(64, 64)
        )

        self.conv3 = nn.Sequential(
            Residual(64, 128, stride=2),
            Residual(128, 128),
            Residual(128, 128),
            Residual(128, 128),
            Residual(128, 128)
        )

        self.conv4 = nn.Sequential(
            Residual(128, 256, stride=2),
            Residual(256, 256),
            Residual(256, 256),
            Residual(256, 256),
            Residual(256, 256),
            Residual(256, 256),
        )

        self.conv5 = nn.Sequential(
            Residual(256, 512, stride=2),
            Residual(512, 512),
            Residual(512, 512)
        )

        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Linear(512, num_classes)

    def forward(self, x):
        out = self.conv1(x)
        out = self.conv2(out)
        out = self.conv3(out)
        out = self.conv4(out)
        out = self.conv5(out)

        out = self.avg_pool(out)
        out = out.reshape(out.shape[0], -1)

        out = self.fc(out)
        return out
    
    def prediction(self, x):
        x = self.forward(x)
        x = nn.functional.softmax(x)

        return x
    

def prediction(datas):
    acc_data = 0
    correct_data = torch.zeros(1).squeeze().cuda()
    total_data = torch.zeros(1).squeeze().cuda()
    for i,data in enumerate(datas):
        X_data, Y_data = data
        X_data = X_data.permute(0, 3, 1, 2)

        X_data = X_data.to(device)
        Y_data = Y_data.to(device)

        Y_hat = net.prediction(X_data)

        prediction = torch.argmax(Y_hat, dim=1)
        correct_data += (prediction == Y_data).sum().float()
        total_data += len(Y_data)
    acc_data = (correct_data / total_data).cpu().detach().data.numpy()

    return acc_data


device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

num_epoch = 50
learning_rate = 0.01
batch_size = 32
costs = []
classes = 6

train_data = Image_Data('DeepLearning/learning_with_AndrewNg/04.卷积神经网络/week2_task/datasets/train_signs.h5')
train_data_loader = DataLoader(train_data, shuffle=True, batch_size=batch_size)

test_data = Image_Data('DeepLearning/learning_with_AndrewNg/04.卷积神经网络/week2_task/datasets/test_signs.h5')
test_data_loader = DataLoader(test_data, shuffle=False, batch_size=batch_size)

net = ResNet(3, num_classes=classes)
net = net.to(device)

Loss = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(net.parameters(), lr=learning_rate)

for epoch in range(num_epoch):
    cost = 0
    for i, data in enumerate(train_data_loader):
        X_data, Y_data = data
        X_data = X_data.permute(0, 3, 1, 2)

        X_data = X_data.to(device)
        Y_data = Y_data.to(device)

        optimizer.zero_grad()

        Y_hat = net.forward(X_data)

        loss = Loss(Y_hat, Y_data.long())

        loss.backward()

        optimizer.step()

        cost = cost + loss.cpu().detach().numpy()
    costs.append(cost /(i + 1))

    if epoch % 5 == 0:
        print(f'第{epoch}次迭代，损失值：{cost / (i + 1)}')


acc_train = prediction(train_data_loader)
acc_test = prediction(test_data_loader)

print(f'训练集准确率：{acc_train}')
print(f'测试集准确率：{acc_test}')

plt.plot(costs)
plt.ylabel('loss')
plt.xlabel('iterations')
plt.title(f'Learning Rate = {learning_rate}')
plt.show()

