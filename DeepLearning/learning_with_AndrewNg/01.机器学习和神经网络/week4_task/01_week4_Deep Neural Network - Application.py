import numpy as np
import h5py
import matplotlib.pyplot as plt
import testCases_v2
import dnn_utils_v2
from dnn_app_utils_v2 import load_data
import cv2

np.random.seed(1)

def initialize_parameters(n_x, n_h, n_y):
    W1 = np.random.randn(n_h, n_x) * 0.01
    b1 = np.zeros(shape=(n_h, 1))
    W2 = np.random.randn(n_y, n_h) * 0.01
    b2 = np.zeros(shape=(n_y, 1))

    assert(W1.shape == (n_h, n_x))
    assert(b1.shape == (n_h, 1))
    assert(W2.shape == (n_y, n_h))
    assert(b2.shape == (n_y, 1))

    parameters = {
        'W1': W1,
        'b1': b1,
        'W2': W2,
        'b2': b2
    }

    return parameters

# print('------测试initialize_parameters------')
# parameters = initialize_parameters(3, 2, 1)
# print(f"W1 = {parameters['W1']}")
# print(f"b1 = {parameters['b1']}")
# print(f"W2 = {parameters['W2']}")
# print(f"b2 = {parameters['b2']}")


def initialize_parameters_deep(layers_dims):
    np.random.seed(3)
    parameters = {}
    L = len(layers_dims)

    for i in range(1, L):
        parameters[f'W{i}'] = np.random.randn(layers_dims[i], layers_dims[i-1]) / np.sqrt(layers_dims[i-1])
        parameters[f'b{i}'] = np.zeros(shape=(layers_dims[i], 1))

        assert(parameters[f'W{i}'].shape == (layers_dims[i], layers_dims[i-1]))
        assert(parameters[f'b{i}'].shape == (layers_dims[i], 1))

    return parameters

def linear_forward(A, W, b):
    Z = np.dot(W, A) + b
    assert(Z.shape == (W.shape[0], A.shape[1]))
    cache = (A, W, b)

    return Z, cache

# print("------测试linear_forward------")
# A, W, b = testCases_v2.linear_forward_test_case()
# Z, cache = linear_forward(A, W, b)
# print(f"Z = {Z}")


def linear_activation_forward(A_prev, W, b, activation):
    if activation == "sigmoid":
        Z, linear_cache = linear_forward(A_prev, W, b)
        A, activation_cache = dnn_utils_v2.sigmoid(Z)
    elif activation == "relu":
        Z, linear_cache = linear_forward(A_prev, W, b)
        A, activation_cache = dnn_utils_v2.relu(Z)

    assert(A.shape == Z.shape)

    cache = (linear_cache, activation_cache)

    return A, cache

# print("------测试linear_activation_forward------")
# A_prev, W, b = testCases_v2.linear_activation_forward_test_case()

# A, cache = linear_activation_forward(A_prev, W, b, activation="sigmoid")
# print(f"sigmoid, A = {A}")

# A, cache = linear_activation_forward(A_prev, W, b, activation="relu")
# print(f"relu, A = {A}")


def L_model_forward(X, parameters):
    caches = []
    A = X
    L = len(parameters) // 2
    for i in range(1, L):
        A_prev = A
        A, cache = linear_activation_forward(A_prev, parameters[f'W{i}'], parameters[f'b{i}'], activation="relu")
        caches.append(cache)

    AL, cache = linear_activation_forward(A, parameters[f'W{L}'], parameters[f'b{L}'], activation="sigmoid")
    caches.append(cache)

    assert(AL.shape == (1, X.shape[1]))

    return AL, caches



def compute_cost(AL, Y):
    m = Y.shape[1]
    cost = (-1 / m) * np.sum(np.multiply(Y, np.log(AL)) + np.multiply((1 - Y), np.log(1 - AL)))

    assert(cost.shape == ())

    return cost

# print("------测试compute_cost------")
# Y, AL = testCases_v2.compute_cost_test_case()
# cost = compute_cost(AL, Y)
# print(f"cost = {cost}")

def linear_backward(dZ, cache):
    A_prev, W, b = cache
    m = A_prev.shape[1]
    dW = np.dot(dZ, A_prev.T) / m
    db = np.sum(dZ, axis=1, keepdims=True) / m
    dA_prev = np.dot(W.T, dZ)

    assert(dW.shape == W.shape)
    assert(db.shape == b.shape)
    assert(dA_prev.shape == A_prev.shape)

    return dA_prev, dW, db

# print("------测试compute_cost------")
# dZ, cache = testCases_v2.linear_backward_test_case()
# dA_prev, dW, db = linear_backward(dZ, cache)
# print(f"dA_prev = {dA_prev}")
# print(f"dW = {dW}")
# print(f"db = {db}")


def linear_activation_backward(dA, cache, activation="relu"):
    linear_cache, activation_cache = cache
    if activation == "relu":
        dZ = dnn_utils_v2.relu_backward(dA, activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache)
    elif activation == "sigmoid":
        dZ = dnn_utils_v2.sigmoid_backward(dA, activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache)

    return dA_prev, dW, db

# print("------测试linear_activation_backward------")
# dA, cache = testCases_v2.linear_activation_backward_test_case()
# dA_prev, dW, db = linear_activation_backward(dA, cache)
# print(f"dA_prev = {dA_prev}")
# print(f"dW = {dW}")
# print(f"db = {db}")


def L_model_backward(AL, Y, caches):
    grads = {}
    L = len(caches)
    m = Y.shape[1]
    dAL = - (np.divide(Y, AL) - np.divide(1-Y, 1-AL))

    current_cache = caches[L-1]
    grads[f'dA{L}'], grads[f'dW{L}'], grads[f'db{L}'] = linear_activation_backward(dAL, current_cache, "sigmoid")

    for i in reversed(range(L-1)):
        current_cache = caches[i]
        grads[f'dA{i+1}'], grads[f'dW{i+1}'], grads[f'db{i+1}'] = linear_activation_backward(grads[f'dA{i+2}'], current_cache, "relu")

    return grads



def update_parameters(parameters, grads, learning_rate):
    L = len(parameters) // 2
    for l in range(L):
        parameters[f'W{l+1}'] = parameters[f'W{l+1}'] - learning_rate * grads[f'dW{l+1}']
        parameters[f'b{l+1}'] = parameters[f'b{l+1}'] - learning_rate * grads[f'db{l+1}']

    return parameters

# print('------测试update_parameters------')
# parameters, grads = testCases_v2.update_parameters_test_case()
# parameters = update_parameters(parameters, grads, 0.1)
# print(f"W1 = {parameters['W1']}")
# print(f"b1 = {parameters['b1']}")
# print(f"W2 = {parameters['W2']}")
# print(f"b2 = {parameters['b2']}")

def two_layer_model(X, Y, layers_dims, learning_rate=0.0075, num_iterations=3000, print_cost=False, isPlot=True):
    np.random.seed(1)
    grads = {}
    costs = []
    (n_x, n_h, n_y) = layers_dims

    parameters = initialize_parameters(n_x, n_h, n_y)

    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']

    for i in range(num_iterations):


        A1, cache1 = linear_activation_forward(X, W1, b1, activation="relu")
        A2, cache2 = linear_activation_forward(A1, W2, b2, activation="sigmoid")

        cost = compute_cost(A2, Y)

        dA2 = - (np.divide(Y, A2) - np.divide(1-Y, 1-A2))

        dA1, dW2, db2 = linear_activation_backward(dA2, cache2, activation="sigmoid")
        dA0, dW1, db1 = linear_activation_backward(dA1, cache1, activation="relu")

        grads['dW1'] = dW1
        grads['db1'] = db1
        grads['dW2'] = dW2
        grads['db2'] = db2

        parameters = update_parameters(parameters, grads, learning_rate)

        W1 = parameters['W1']
        b1 = parameters['b1']
        W2 = parameters['W2']
        b2 = parameters['b2']


        if print_cost:
            if i % 100 == 0:
                costs.append(cost)
                print(f"迭代次数：{i}，损失值：{cost}")

    if isPlot:
        plt.plot(costs)
        plt.ylabel('cost')
        plt.xlabel('iterations')
        plt.title(f"Learning rate = {learning_rate}")

    return parameters               


def L_layer_model(X, Y, layers_dims, learning_rate= 0.0075, num_iterations=3000, print_cost=False, isPlot=True):
    np.random.seed(1)
    costs = []
    
    parameters = initialize_parameters_deep(layers_dims)


    for i in range(num_iterations):


        AL, caches = L_model_forward(X, parameters)

        cost = compute_cost(AL, Y)

        grads = L_model_backward(AL, Y, caches)

        parameters = update_parameters(parameters, grads, learning_rate)


        if print_cost:
            if i % 100 == 0:
                costs.append(cost)
                print(f"迭代次数：{i}，损失值：{cost}")

    if isPlot:
        plt.plot(costs)
        plt.ylabel('cost')
        plt.xlabel('iterations')
        plt.title(f"Learning rate = {learning_rate}")

    return parameters


def predict(X, Y, parameters):

    m = X.shape[1]

    AL, caches = L_model_forward(X, parameters)

    for i in range(AL.shape[1]):
        if AL[0, i] > 0.5:
            AL[0, i] = 1
        else:
            AL[0, i] = 0
    
    p = (m - np.sum(np.abs(Y-AL))) / m
    
    return p, AL


if __name__ == "__main__":
    train_set_x_orig, train_y, test_set_x_orig, test_y, classes = load_data()
    train_set_x = train_set_x_orig.reshape(train_set_x_orig.shape[0], -1).T
    test_set_x = test_set_x_orig.reshape(test_set_x_orig.shape[0], -1).T
    train_x = train_set_x / 255
    test_x = test_set_x / 255

    # layers_dims = [train_x.shape[0], 7, 1]
    # parameters = two_layer_model(train_x, train_y, layers_dims, num_iterations=2500, print_cost=True)

    layers_dims = [train_x.shape[0], 20, 7, 5, 1]
    parameters = L_layer_model(train_x, train_y, layers_dims, learning_rate=0.0075, num_iterations=1000, print_cost=True)

    p_train, pre_train_y = predict(train_x, train_y, parameters)
    p_test, pre_test_y = predict(test_x, test_y, parameters)

    print(f"训练集准确率：{p_train}")
    print(f"测试集准确率：{p_test}")
    plt.show()

    img = cv2.imread("DeepLearning/learning_with_AndrewNg/week4_task/datasets/2.jpeg")
    img = cv2.resize(img, (64, 64))
    img = img.reshape(1, -1).T
    y = [1]
    p, pre_y = predict(img, y, parameters)
    # print(f'{int(pre_y[0, 0])}')
    print(f"{classes[int(pre_y[0, 0])]}")
