import torch.nn as nn


class Encoder(nn.Module):
    def __init__(self, input_dim, hidden_dim, out_dim):
        super(Encoder, self).__init__()
        self.layer1 = nn.Sequential(nn.Linear(input_dim, hidden_dim),
                                    nn.ReLU())
        self.layer2 = nn.Sequential(nn.Linear(hidden_dim, out_dim),
                                    nn.ReLU())

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)

        return x