import numpy as np
import matplotlib.pyplot as plt
import opt_utils
import math


def update_parameters_with_gd(parameters, grads, learning_rate):
    L = len(parameters) // 2
    for l in range(1, L+1):
        parameters[f'W{l}'] = parameters[f'W{l}'] - learning_rate * grads[f'dW{l}']
        parameters[f'b{l}'] = parameters[f'b{l}'] - learning_rate * grads[f'db{l}']

    return parameters    


def initialize_momentun(parameters):
    v = {}
    L = len(parameters) // 2
    for l in range(1, L+1):
        v[f'dW{l}'] = np.zeros_like(parameters[f'W{l}'])
        v[f'db{l}'] = np.zeros_like(parameters[f'b{l}'])

    return v


def update_parameters_with_momentun(parameters, grads, v, beta, learning_rate):
    L = len(parameters) // 2
    for l in range(1, L+1):
        v[f'dW{l}'] = beta * v[f'dW{l}'] + (1-beta) * grads[f'dW{l}']
        v[f'db{l}'] = beta * v[f'db{l}'] + (1-beta) * grads[f'db{l}']

        parameters[f'W{l}'] = parameters[f'W{l}'] - learning_rate * v[f'dW{l}']
        parameters[f'b{l}'] = parameters[f'b{l}'] - learning_rate * v[f'db{l}']

    return parameters


def initialize_Adam(parameters):
    v = {}
    s = {}
    L = len(parameters) // 2
    for l in range(1, L+1):
        v[f'dW{l}'] = np.zeros_like(parameters[f'W{l}'])
        v[f'db{l}'] = np.zeros_like(parameters[f'b{l}'])

        s[f'dW{l}'] = np.zeros_like(parameters[f'W{l}'])
        s[f'db{l}'] = np.zeros_like(parameters[f'b{l}'])

    return (v, s)

def update_parameters_with_Adam(parameters, grads, v, s, t, beta1, beta2, learning_rate, epsilon=1e-8):
    L = len(parameters) // 2
    v_corrected = {}
    s_corrected = {}
    for l in range(1, L+1):
        v[f'dW{l}'] = beta1 * v[f'dW{l}'] + (1-beta1) * grads[f'dW{l}']
        v[f'db{l}'] = beta1 * v[f'db{l}'] + (1-beta1) * grads[f'db{l}']

        v_corrected[f'dW{l}'] = v[f'dW{l}'] / (1 - np.power(beta1, t))
        v_corrected[f'db{l}'] = v[f'db{l}'] / (1 - np.power(beta1, t))

        s[f'dW{l}'] = beta2 * s[f'dW{l}'] + (1-beta2) * np.square(grads[f'dW{l}'])
        s[f'db{l}'] = beta2 * s[f'db{l}'] + (1-beta2) * np.square(grads[f'db{l}'])

        s_corrected[f'dW{l}'] = s[f'dW{l}'] / (1 - np.power(beta2, t))
        s_corrected[f'db{l}'] = s[f'db{l}'] / (1 - np.power(beta2, t))

        parameters[f'W{l}'] = parameters[f'W{l}'] - learning_rate * (v_corrected[f'dW{l}'] / (np.sqrt(s_corrected[f'dW{l}']) + epsilon))
        parameters[f'b{l}'] = parameters[f'b{l}'] - learning_rate * (v_corrected[f'db{l}'] / (np.sqrt(s_corrected[f'db{l}']) + epsilon))

    return parameters, v, s


def random_mini_batches(X, Y, mini_batch_size=64):
    mini_batches = []
    m = X.shape[1]

    permutation = list(np.random.permutation(m))
    X_shuffled = X[:, permutation]
    Y_shuffled = Y[:, permutation]

    num_minibatches = math.floor(m / mini_batch_size)
    for i in range(num_minibatches):
        mini_batch_X = X_shuffled[:, i*mini_batch_size:(i+1)*mini_batch_size]
        mini_batch_Y = Y_shuffled[:, i*mini_batch_size:(i+1)*mini_batch_size]

        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)
    
    if m % mini_batch_size != 0:
        mini_batch_X = X_shuffled[:, num_minibatches*mini_batch_size:]
        mini_batch_Y = Y_shuffled[:, num_minibatches*mini_batch_size:]

        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)

    return mini_batches


def model(X, Y, layers_dims, optimizer, beta1=0.9, beta2=0.999, learning_rate=0.3, mini_batch_size=64, num_epochs=10000):
    m = X.shape[1]
    costs = []
    t = 0

    parameters = opt_utils.initialize_parameters(layers_dims)

    if optimizer == 'gd':
        pass
    elif optimizer == 'momentun':
        v = initialize_momentun(parameters)
    elif optimizer == 'Adam':
        v, s = initialize_Adam(parameters)
    else:
        print('error')

    for epoch in range(num_epochs):

        mini_batches = random_mini_batches(X, Y, mini_batch_size)
        
        for mini_batch in mini_batches:

            (mini_batch_X, mini_batch_Y) = mini_batch
            Y_hat, cache = opt_utils.forward_propagation(mini_batch_X, parameters)

            loss = opt_utils.compute_cost(Y_hat, mini_batch_Y)

            grads = opt_utils.backward_propagation(mini_batch_X, mini_batch_Y, cache)

            if optimizer == 'gd':
                parameters = update_parameters_with_gd(parameters, grads, learning_rate)
            elif optimizer == 'momentun':
                parameters = update_parameters_with_momentun(parameters, grads, v, beta1, learning_rate)
            elif optimizer == 'Adam':
                t = t + 1
                parameters, v, s = update_parameters_with_Adam(parameters, grads, v, s, t, beta1, beta2, learning_rate)

        if epoch % 100 == 0:
            costs.append(loss)
            print(f"第{epoch}次迭代， 损失值：{loss}")

    plt.plot(costs)
    plt.xlabel('iterations')
    plt.ylabel('loss')
    plt.title(f'Learning Rate = {learning_rate}')
    plt.show()

    return parameters


train_X, train_Y = opt_utils.load_dataset()
print(train_X.shape)
plt.show()

layers_dims = [2, 5, 2, 1]
parameters = model(train_X, train_Y, layers_dims, optimizer='Adam',
                   beta1=0.9, beta2=0.999, learning_rate=0.0007, mini_batch_size=64, num_epochs=10000)

preditions = opt_utils.predict(train_X,train_Y,parameters)

axes = plt.gca()
axes.set_xlim([-1.5, 2.5])
axes.set_ylim([-1, 1.5])
opt_utils.plot_decision_boundary(lambda x: opt_utils.predict_dec(parameters, x.T), train_X, train_Y)