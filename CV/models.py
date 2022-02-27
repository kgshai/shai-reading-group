import torch
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

class MLP(torch.nn.Module):
    
    def __init__(self, input_dim, output_dim, num_nodes, num_layers, act=torch.nn.ReLU()):
        super().__init__()
        self.layers = torch.nn.ModuleList()
        assert num_layers > 0
        for i in range(num_layers):
            in_dim = input_dim if i == 0 else num_nodes
            out_dim = output_dim if i == num_layers - 1 else num_nodes
            self.layers.append(torch.nn.Linear(in_dim, out_dim))
            if i != num_layers - 1:
                self.layers.append(act)
        
    def forward(self, x):
        for mod in self.layers:
            x = mod(x)
        return x
        
class SVDLinearCondense(torch.nn.Module):
    
    def __init__(self, in_dim, out_dim):
        super().__init__()
        assert out_dim < in_dim
        self.in_dim = in_dim
        self.out_dim = out_dim
        self.u = torch.nn.Parameter(torch.randn(in_dim, in_dim))
        self.s = torch.nn.Parameter(torch.randn(out_dim))
        self.v = torch.nn.Parameter(torch.randn(out_dim, out_dim))
        self.w = torch.nn.Parameter(torch.randn(in_dim - out_dim))
        self.bias = torch.nn.Parameter(torch.randn(out_dim))
        
    def forward(self, x):
        x = torch.matrix_exp((self.u - self.u.T) / 2) @ x
        x = x[..., :self.out_dim] * self.s
        x = torch.matrix_exp((self.v - self.v.T) / 2) @ x
        x = x + self.bias
        return x
    
    def backward(self, x):
        x = x - self.bias
        x = torch.matrix_exp((self.v.T - self.v) / 2) @ x
        x = x * self.s
        x = torch.concat([x, self.w])
        x = torch.matrix_exp((self.u.T - self.u) / 2) @ x
        return x
        
        
class SVDVAE(torch.nn.Module):
    
    def __init__(self, input_dim, latent_dim, num_nodes, num_layers, act=torch.nn.ReLU()):
        super().__init__()
        self.layers = torch.nn.ModuleList()
        assert num_layers > 0
        for i in range(num_layers):
            in_dim = input_dim if i == 0 else num_nodes
            out_dim = latent_dim if i == num_layers - 1 else num_nodes
            self.layers.append(SVDLinearCondense(in_dim, out_dim))
            if i != num_layers - 1:
                self.layers.append(act)
        self.std = torch.nn.Parameter(torch.randn(latent_dim))
        
    def encode(self, x):
        for mod in self.layers:
            x = mod(x)
        return x
    
    def decode(self, x):
        for mod in reversed(self.layers):
            x = mod.backward(x)
        return x

    def forward(self, x):
        mu = self.encode(x)
        x = mu + self.std * torch.randn_like(self.std)
        x = self.decode(x)
        return x, mu, self.std
        
class VAE(torch.nn.Module):
    
    def __init__(self, data_dim, latent_dim, num_nodes, num_layers, act=torch.nn.ReLU()):
        super().__init__()
        self.encoder = MLP(data_dim, latent_dim, num_nodes, num_layers, act)
        self.decoder = MLP(latent_dim, data_dim, num_nodes, num_layers, act)
        self.std = torch.randn(latent_dim)
        
    def forward(self, x):
        mu = self.encoder(x)
        x = mu + self.std * torch.randn_like(self.std)
        x = self.decoder(x)
        return x, mu, self.std
    
A = torch.randn((3, 2))
x = torch.randn((100, 2))
y = x @ A.T
plt.scatter(y[:, 0], y[:, 1], y[:, 2])
plt.show()