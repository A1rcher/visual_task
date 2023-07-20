import numpy as np
import matplotlib.pyplot as plt
import reg_utils

def dropout(X, keep_prob):
    mask = np.random.rand(X.shape[0], X.shape[1]) < keep_prob
    return mask * X / keep_prob

def forward_propagation_dropout(X, parameters, keep_prob):
    W1 = parameters["W1"]
    b1 = parameters["b1"]
    W2 = parameters["W2"]
    b2 = parameters["b2"]
    W3 = parameters["W3"]
    b3 = parameters["b3"]    

    Z1 = np.dot(W1, X) + b1
    A1 = reg_utils.relu(Z1)
    A1 = dropout(A1, keep_prob)
    Z2 = np.dot(W2, A1) + b2
    A2 = reg_utils.relu(Z2)
    A2 = dropout(A2, keep_prob)
    Z3 = np.dot(W3, A2) + b3
    A3 = reg_utils.sigmoid(Z3)
    
    cache = (Z1, A1, W1, b1, Z2, A2, W2, b2, Z3, A3, W3, b3)
    
    return A3, cache    

def compute_cost__L2(A3, Y, parameters, lambd):
    m = Y.shape[1]
    W1 = parameters['W1']
    W2 = parameters['W2']
    W3 = parameters['W3']

    logprobs = np.multiply(-np.log(A3),Y) + np.multiply(-np.log(1 - A3), 1 - Y)
    cost = 1./m * np.nansum(logprobs) + (lambd / (2 * m)) * (np.sum(np.square(W1)) + np.sum(np.square(W2)) + np.sum(np.square(W3)))

    return cost

def backward_L2_dropout(X, Y, cache, lambd, keep_prob):
    m = X.shape[1]
    (Z1, A1, W1, b1, Z2, A2, W2, b2, Z3, A3, W3, b3) = cache
    
    dZ3 = A3 - Y
    dW3 = 1./m * np.dot(dZ3, A2.T) + (lambd * W3) / m
    db3 = 1./m * np.sum(dZ3, axis=1, keepdims = True)
    
    dA2 = np.dot(W3.T, dZ3)
    dA2 = dropout(dA2, keep_prob)
    dZ2 = np.multiply(dA2, np.int64(A2 > 0))
    dW2 = 1./m * np.dot(dZ2, A1.T) + (lambd * W2) / m
    db2 = 1./m * np.sum(dZ2, axis=1, keepdims = True)
    
    dA1 = np.dot(W2.T, dZ2)
    dA1 = dropout(dA1, keep_prob)
    dZ1 = np.multiply(dA1, np.int64(A1 > 0))
    dW1 = 1./m * np.dot(dZ1, X.T) + (lambd * W1) / m
    db1 = 1./m * np.sum(dZ1, axis=1, keepdims = True)
    
    gradients = {"dZ3": dZ3, "dW3": dW3, "db3": db3,
                 "dA2": dA2, "dZ2": dZ2, "dW2": dW2, "db2": db2,
                 "dA1": dA1, "dZ1": dZ1, "dW1": dW1, "db1": db1}
    
    return gradients


def model(X, Y, learning_rate=0.3, num_iterations=30000, lambd=0, keep_prob=1):
    grads = {}
    costs = []
    
    parameters = reg_utils.initialize_parameters(layer_dims)
    
    for i in range(num_iterations):
        
        Y_hat, cache = forward_propagation_dropout(X, parameters, keep_prob)

        loss = compute_cost__L2(Y_hat, Y, parameters, lambd)

        grads = backward_L2_dropout(X, Y, cache, lambd, keep_prob)

        parameters = reg_utils.update_parameters(parameters, grads, learning_rate)

        if i % 1000 == 0:
            costs.append(loss)
            print(f'第{i}次迭代，损失值：{loss}')

    plt.plot(costs)
    plt.xlabel('iterations')
    plt.ylabel('loss')
    plt.title(f'Learning Rate = {learning_rate}')
    plt.show()

    return parameters




train_X, train_Y, test_X, test_Y = reg_utils.load_2D_dataset()
print(train_X.shape)

layer_dims = [2, 32, 16, 1]

parameters = model(train_X, train_Y, learning_rate=0.3, lambd=0, keep_prob=1)

predictions_train = reg_utils.predict(train_X, train_Y, parameters)
predictions_test = reg_utils.predict(test_X, test_Y, parameters)

axes = plt.gca()
axes.set_xlim([-0.75, 0.40])
axes.set_ylim([-0.75, 0.65])
reg_utils.plot_decision_boundary(lambda x: reg_utils.predict_dec(parameters, x.T), train_X, train_Y)
