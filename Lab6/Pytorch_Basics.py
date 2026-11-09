"""PyTorch tensor operations, autograd and simple linear regression."""
import torch

def tensor_demo():
    x=torch.tensor([1.,2.,3.],requires_grad=True)
    y=(x*x).sum()
    y.backward()
    print("Tensor:",x)
    print("Gradient:",x.grad)

def linear_regression():
    torch.manual_seed(0)
    X=torch.linspace(0,10,100).reshape(-1,1)
    y=3*X+2+torch.randn_like(X)*0.5
    model=torch.nn.Linear(1,1)
    optimizer=torch.optim.SGD(model.parameters(),lr=.01)
    loss_fn=torch.nn.MSELoss()
    for epoch in range(500):
        pred=model(X); loss=loss_fn(pred,y)
        optimizer.zero_grad(); loss.backward(); optimizer.step()
    print("Learned weight/bias:",model.weight.item(),model.bias.item())
    print("Final loss:",loss.item())
    torch.save(model.state_dict(),"models/linear_regression.pt")

if __name__=="__main__":
    tensor_demo(); linear_regression()
