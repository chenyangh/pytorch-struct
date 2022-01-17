import torch
import numpy as np
import math

N = 8
D = int(math.log(N))


tree_prob = torch.zeros(N*D, N)

tree_prob[0] = torch.arange(N)

