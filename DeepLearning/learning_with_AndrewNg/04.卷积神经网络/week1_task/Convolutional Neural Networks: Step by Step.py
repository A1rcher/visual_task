import numpy as np
import matplotlib.pyplot as plt
import cnn_utils

def zero_pad(X, pad):
    X_paded = np.pad(X, ((0, 0), (pad, pad), (pad, pad), (0, 0)), 'constant', constant_values=0)

    return X_paded

# x = np.random.randn(4, 3, 3, 2)
# x_paded = zero_pad(x, 2)

# print('x.shape = ', x.shape)
# print('x_paded.shape = ', x_paded.shape)
# print('x[1, 1] = ', x[1, 1])
# print('x_paded[1, 1] = ', x_paded[1, 1])

# fig, axarr = plt.subplots(1, 2)
# axarr[0].set_title('x')
# axarr[0].imshow(x[0,:,:,0])
# axarr[1].set_title('x_paded')
# axarr[1].imshow(x_paded[0,:,:,0])
# plt.show()

def conv_single_step(a_slice_prev, W, b):
    s = np.multiply(a_slice_prev, W) + b
    Z = np.sum(s)

    return Z


def conv_forward(A_prev, W, b, hparameters):
    (m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape

    (f, f, n_C_prev, n_C) = W.shape

    stride = hparameters['stride']
    pad = hparameters['pad']

    n_H = int((n_H_prev - f + 2 * pad)/stride) + 1
    n_W = int((n_W_prev - f + 2 * pad)/stride) + 1

    Z = np.zeros((m, n_H, n_W, n_C))

    A_prev_pad = zero_pad(A_prev, pad)

    for i in range(m):
        a_prev_pad = A_prev_pad[i]
        for h in range(n_H):
            for w in range(n_W):
                for c in range(n_C):
                    vert_start = h * stride
                    vert_end = vert_start + f
                    horiz_start = w * stride
                    horiz_end = horiz_start + f

                    a_slice_prev = a_prev_pad[vert_start:vert_end, horiz_start:horiz_end,:]

                    Z[i, h, w, c] = conv_single_step(a_slice_prev, W[:,:,:,c], b[0,0,0,c])

    assert(Z.shape == (m, n_H, n_W, n_C))

    cache = (A_prev, W, b, hparameters)

    return Z, cache

# np.random.seed(1)

# A_prev = np.random.randn(10,4,4,3)
# W = np.random.randn(2,2,3,8)
# b = np.random.randn(1,1,1,8)

# hparameters = {"pad" : 2, "stride": 1}

# Z , cache_conv = conv_forward(A_prev,W,b,hparameters)

# print("np.mean(Z) = ", np.mean(Z))
# print("cache_conv[0][1][2][3] =", cache_conv[0][1][2][3])

def pool_forward(A_prev, hparameters, mode='max'):
    (m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape

    f = hparameters['f']
    stride = hparameters['stride']

    n_H = int((n_H_prev - f) / stride) + 1
    n_W = int((n_W_prev - f) / stride) + 1
    n_C = n_C_prev

    Z = np.zeros((m, n_H, n_W, n_C))

    for i in range(m):
        for h in range(n_H):
            for w in range(n_W):
                for c in range(n_C):
                    vert_start = h * stride
                    vert_end = vert_start + f
                    horiz_start = w * stride
                    horiz_end = horiz_start + f

                    a_slice_prev = A_prev[i, vert_start:vert_end, horiz_start:horiz_end, c]

                    if mode == 'max':
                        Z[i, h, w, c] = np.max(a_slice_prev)
                    elif mode =='average':
                        Z[i, h, w, c] = np.mean(a_slice_prev)

    assert(Z.shape == (m, n_H, n_W, n_C))

    cache = (A_prev, hparameters)

    return Z, cache
    
# np.random.seed(1)
# A_prev = np.random.randn(2,4,4,3)
# hparameters = {"f":4 , "stride":1}

# A , cache = pool_forward(A_prev,hparameters,mode="max")
# A, cache = pool_forward(A_prev, hparameters)
# print("mode = max")
# print("A =", A)
# print("----------------------------")
# A, cache = pool_forward(A_prev, hparameters, mode = "average")
# print("mode = average")
# print("A =", A)

