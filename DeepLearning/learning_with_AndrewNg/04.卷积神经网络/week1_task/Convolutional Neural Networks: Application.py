import numpy as np
import matplotlib.pyplot as plt
import cnn_utils
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import torch.utils.data
import h5py

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class Digit_data(torch.utils.data.Dataset):
    def __init__(self, data_path):
        super(Digit_data, self).__init__()
        dataset = h5py.File(data_path, "r")
        if data_path == "DeepLearning/learning_with_AndrewNg/04.卷积神经网络/week1_task/datasets/train_signs.h5":
            dataset_set_x_orig = np.array(dataset["train_set_x"][:])  # your train set features
            dataset_set_y_orig = np.array(dataset["train_set_y"][:])  # your train set labels
        else:
            dataset_set_x_orig = np.array(dataset["test_set_x"][:])  # your train set features
            dataset_set_y_orig = np.array(dataset["test_set_y"][:])  # your train set labels

        dataset_set_x_orig = dataset_set_x_orig.astype("float32") / 255
        dataset_set_y_orig = dataset_set_y_orig.astype("float32")

        self.x_data = torch.from_numpy(dataset_set_x_orig)
        self.y_data = torch.from_numpy(dataset_set_y_orig)

        self.len = self.y_data.size()[0]

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.len
    



# X_train = np.transpose(train_set_x_orig, (0, 3, 1, 2)) / 255
# Y_train = np.eye(6)[train_set_y_orig.reshape(-1)]
# print(test_set_x_orig.shape)
# print(train_set_y_orig.shape)
# print(Y_train.shape)


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)

        self.fc1 = nn.Linear(16*13*13, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 6)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), 2)
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.reshape(x.shape[0], -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)

        return x
    
    def test(self, x):
        x = self.forward(x)
        x = F.softmax(x)

        return x


num_epoch = 200
learning_rate = 0.00095
mini_batch_size = 32
costs = []

train_data = Digit_data('DeepLearning/learning_with_AndrewNg/04.卷积神经网络/week1_task/datasets/train_signs.h5')
train_data_loader = torch.utils.data.DataLoader(train_data, shuffle=True, batch_size=mini_batch_size)

net = Net()
net = net.to(device)
Loss = nn.CrossEntropyLoss()

optimizer = optim.Adam(net.parameters(), lr=learning_rate)


for epoch in range(100):
    cost = 0
    for i, data in enumerate(train_data_loader):
        mini_batch_X, mini_batch_Y = data
        mini_batch_X = mini_batch_X.permute(0, 3, 1, 2)
        mini_batch_X, mini_batch_Y = mini_batch_X.to(device), mini_batch_Y.to(device)

        optimizer.zero_grad()

        Y_hat = net.forward(mini_batch_X)

        loss = Loss(Y_hat, mini_batch_Y.long())

        loss.backward()
        optimizer.step()

        cost = cost + loss.cpu().detach().numpy()
    costs.append(cost / (i+1))
    if epoch % 5 == 0:
        print(f'第{epoch}次迭代，损失值：{cost / (i+1)}')

test_data = Digit_data('DeepLearning/learning_with_AndrewNg/04.卷积神经网络/week1_task/datasets/test_signs.h5')
test_data_loader = torch.utils.data.DataLoader(test_data, shuffle=False, batch_size=mini_batch_size)


acc_train = 0
acc_test = 0
correct_train = torch.zeros(1).squeeze().cuda()
total_train = torch.zeros(1).squeeze().cuda()
for i, data in enumerate(train_data_loader):
    mini_batch_X, mini_batch_Y = data
    mini_batch_X = mini_batch_X.permute(0, 3, 1, 2)
    mini_batch_X, mini_batch_Y = mini_batch_X.to(device), mini_batch_Y.to(device)

    pred = net.test(mini_batch_X)

    prediction = torch.argmax(pred, dim=1)

    correct_train += (prediction == mini_batch_Y).sum().float()
    total_train += len(mini_batch_Y)

acc_train = (correct_train / total_train).cpu().detach().data.numpy()

print(f"训练集上的准确率：{acc_train}")


correct_test = torch.zeros(1).squeeze().cuda()
total_test = torch.zeros(1).squeeze().cuda()
for i, data in enumerate(test_data_loader):
    mini_batch_X, mini_batch_Y = data
    mini_batch_X = mini_batch_X.permute(0, 3, 1, 2)
    mini_batch_X, mini_batch_Y = mini_batch_X.to(device), mini_batch_Y.to(device)

    pred = net.test(mini_batch_X)

    prediction = torch.argmax(pred, dim=1)

    correct_test += (prediction == mini_batch_Y).sum().float()
    total_test += len(mini_batch_Y)

acc_train = (correct_test / total_test).cpu().detach().data.numpy()

print(f"测试集上的准确率：{acc_train}")


plt.plot(costs)
plt.ylabel('cost')
plt.xlabel('iterations (per tens)')
plt.show()
        


        