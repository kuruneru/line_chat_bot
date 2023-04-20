import numpy as np
import torch
 
n = np.array([1, 2, 3])
a = torch.from_numpy(n.astype(np.float32)).clone()
print(a)