import torch
from torchvision import datasets, transforms
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
import matplotlib.pyplot as plt
import torch.nn.functional as F
import torch.optim as optim
from model import *

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

# 设置一些超参数
batch_size = 64
num_epochs = 3
learning_rate = 0.001
seed = 2
torch.manual_seed(seed)

# 导入数据
train_dataset = datasets.MNIST('DeepLearning/task/first/data', train=True, transform=transforms.ToTensor(), download=True)
test_dataset = datasets.MNIST('DeepLearning/task/first/data', train=False, transform=transforms.ToTensor(), download=True)
train_data_size = len(train_dataset)
test_data_size = len(test_dataset)
train_dataset_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_dataset_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

data = enumerate(train_dataset_loader)
_, (X_data, Y_data) = next(data)
print(X_data)
print(Y_data)
plt.imshow(X_data[4,0,:,:], cmap='gray')
plt.show()


# 选择模型
net = Net()
net = net.to(device)

# 选择损失函数
loss_fn = nn.CrossEntropyLoss()

# 选择优化器
optimizer = optim.Adam(net.parameters(), lr=learning_rate)

costs = []      # 存储损失函数的值

for epoch in range(num_epochs):
    print(f'--------第{epoch+1}轮训练--------')

    # 开始训练
    net.train()
    for i, data in enumerate(train_dataset_loader):
        X_data, Y_data = data
        X_data, Y_data = X_data.to(device), Y_data.to(device)

        optimizer.zero_grad()

        Y_hat = net(X_data)

        loss = loss_fn(Y_hat, Y_data)

        loss.backward()

        optimizer.step()

        if i % 100 == 0:
            costs.append(loss.cpu().detach().numpy())
            print(f'第{i:3d}次，损失值：{loss.cpu().detach().numpy()}')

    # 测试验证集
    net.eval()
    with torch.no_grad():
        correct_acc = 0
        total_loss = 0
        for i, data in enumerate(test_dataset_loader):
            X_data, Y_data = data
            X_data, Y_data = X_data.to(device), Y_data.to(device)       

            Y_hat = net(X_data)
            Y_hat = F.softmax(Y_hat, dim=1)

            loss = loss_fn(Y_hat, Y_data)

            Y_hat = torch.argmax(Y_hat, dim=1)

            total_loss += loss.cpu().detach().numpy()
            correct_acc += (Y_hat == Y_data).sum().float()

        print(f'测试集总loss：{total_loss}')
        print(f"测试集准确率：{correct_acc / test_data_size}")

plt.plot(costs)
plt.xlabel('iterations')
plt.ylabel('loss')
plt.title(f"Learning Rate = {learning_rate}")
plt.show()