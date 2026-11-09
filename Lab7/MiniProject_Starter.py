"""Mini-project starter: traffic-sign / medical-image / placement classification."""
from pathlib import Path
import torch
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader

def train_image_classifier(data_dir="datasets/image_data", num_classes=2, epochs=3):
    transform=transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.Normalize([.485,.456,.406],[.229,.224,.225])
    ])
    dataset=datasets.ImageFolder(data_dir,transform=transform)
    loader=DataLoader(dataset,batch_size=16,shuffle=True)
    model=models.resnet18(weights=None)
    model.fc=torch.nn.Linear(model.fc.in_features,num_classes)
    device="cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    optimizer=torch.optim.Adam(model.parameters(),lr=1e-3)
    loss_fn=torch.nn.CrossEntropyLoss()
    for epoch in range(epochs):
        model.train(); total=0
        for images,labels in loader:
            images,labels=images.to(device),labels.to(device)
            optimizer.zero_grad(); loss=loss_fn(model(images),labels)
            loss.backward(); optimizer.step(); total+=loss.item()
        print(f"Epoch {epoch+1}/{epochs}: loss={total/len(loader):.4f}")
    Path("models").mkdir(exist_ok=True)
    torch.save(model.state_dict(),"models/mini_project_resnet.pt")
    return model

if __name__=="__main__":
    print("Arrange images as datasets/image_data/class_name/image.jpg")
    print("Call train_image_classifier() after adding your dataset.")
