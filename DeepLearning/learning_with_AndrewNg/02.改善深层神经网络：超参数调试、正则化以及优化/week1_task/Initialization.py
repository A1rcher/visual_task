import numpy as np
import matplotlib.pyplot as plt
import init_utils


def initialization_zeros(layers_dims):
    parameters = {}
    L = len(layers_dims)
    for l in range(1, L):
        parameters[f'W{l}'] = np.zeros((layers_dims[l], layers_dims[l-1]))
        parameters[f'b{l}'] = np.zeros((layers_dims[l], 1))

        assert(parameters[f'W{l}'].shape == (layers_dims[l], layers_dims[l-1]))
        assert(parameters[f'b{l}'].shape == (layers_dims[l], 1))

    return parameters

def initialization_random(layers_dims):
    parameters = {}
    L = len(layers_dims)
    for l in range(1, L):
        parameters[f'W{l}'] = np.random.randn(layers_dims[l], layers_dims[l-1]) * 0.01
        parameters[f'b{l}'] = np.zeros((layers_dims[l], 1))

        assert(parameters[f'W{l}'].shape == (layers_dims[l], layers_dims[l-1]))
        assert(parameters[f'b{l}'].shape == (layers_dims[l], 1))
    
    return parameters

def initialization_he(layers_dims):
    parameters = {}
    L = len(layers_dims)
    for l in range(1, L):
        parameters[f'W{l}'] = np.random.randn(layers_dims[l], layers_dims[l-1]) * np.sqrt(2 / layers_dims[l-1])
        parameters[f'b{l}'] = np.zeros((layers_dims[l], 1))

        assert(parameters[f'W{l}'].shape == (layers_dims[l], layers_dims[l-1]))
        assert(parameters[f'b{l}'].shape == (layers_dims[l], 1))

    return parameters

def model(X, Y, learning_rate=0.01, num_iterations=15000, initialization='he', is_plot=True):

    grads = {}
    costs = []

    if initialization == 'zeros':
        parameters = initialization_zeros(layers_dims)
    elif initialization == 'random':
        parameters = initialization_random(layers_dims)
    elif initialization == 'he':
        parameters = initialization_he(layers_dims)
    else:
        print('error')

    for i in range(num_iterations):
        Y_hat, cache = init_utils.forward_propagation(X, parameters)

        loss = init_utils.compute_loss(Y_hat, Y)

        grads = init_utils.backward_propagation(X, Y, cache)

        parameters = init_utils.update_parameters(parameters, grads, learning_rate=learning_rate)

        if i % 1000 == 0:
            costs.append(loss)
            print(f"第{i}次迭代，损失值：{loss}")

    if is_plot:
        plt.plot(costs)
        plt.xlabel('iterations')
        plt.ylabel('loss')
        plt.title(f"Learning rate = {learning_rate}")
        plt.show()

    return parameters

train_X, train_Y, test_X, test_Y = init_utils.load_dataset()
print(train_X.shape)
print(test_X.shape)

layers_dims = 2, 32, 16, 1

parameters = model(train_X, train_Y, initialization='he')

predictions_train = init_utils.predict(train_X, train_Y, parameters)
predictions_test = init_utils.predict(test_X, test_Y, parameters)

axes = plt.gca()
axes.set_xlim([-1.5, 1.5])
axes.set_ylim([-1.5, 1.5])
init_utils.plot_decision_boundary(lambda x: init_utils.predict_dec(parameters, x.T), train_X, train_Y)