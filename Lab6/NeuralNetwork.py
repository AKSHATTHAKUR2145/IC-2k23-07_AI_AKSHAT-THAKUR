"""Small neural network for a synthetic classification dataset."""
import torch
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X,y=make_moons(n_samples=1000,noise=.2,random_state=42)
X=StandardScaler().fit_transform(X)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,random_state=42)
X_train=torch.tensor(X_train,dtype=torch.float32); y_train=torch.tensor(y_train,dtype=torch.float32).view(-1,1)
X_test=torch.tensor(X_test,dtype=torch.float32); y_test=torch.tensor(y_test,dtype=torch.float32).view(-1,1)

model=torch.nn.Sequential(torch.nn.Linear(2,16),torch.nn.ReLU(),torch.nn.Linear(16,8),torch.nn.ReLU(),torch.nn.Linear(8,1))
loss_fn=torch.nn.BCEWithLogitsLoss(); optimizer=torch.optim.Adam(model.parameters(),lr=.01)
for epoch in range(300):
    logits=model(X_train); loss=loss_fn(logits,y_train)
    optimizer.zero_grad(); loss.backward(); optimizer.step()
with torch.no_grad():
    pred=(torch.sigmoid(model(X_test))>=.5).float()
    print("Test accuracy:",(pred==y_test).float().mean().item())
torch.save(model.state_dict(),"models/moons_nn.pt")
