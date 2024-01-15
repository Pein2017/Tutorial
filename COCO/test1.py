import torch
import torch_npu
a = torch.randn(3, 4).npu()
print(a + a)