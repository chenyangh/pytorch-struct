import torch
import numpy as np
import math

N = 8
D = int(math.log2(N)) + 1


tree_prob = torch.zeros(N*D, N)

tree_prob[0] = torch.arange(N)

action_prob = torch.sigmoid(torch.randn(4, N))

# NOTE: Init
_d = 4
start = (_d - 1) * N
end = _d * N - 1
for i in range(start, end + 1):
    tree_prob[i] = torch.sigmoid(torch.randn(N))

for _d in range(D-1, -1, -1):
    start = (_d - 1) * N
    end = _d * N - 1
    for i in range(start, end + 1):
        tmp = 0



