"""ResNet transfer-learning starter using torchvision."""
import torch
from torchvision import models

def build_resnet(num_classes=2, pretrained=False):
    weights=models.ResNet18_Weights.DEFAULT if pretrained else None
    model=models.resnet18(weights=weights)
    for param in model.parameters(): param.requires_grad=False
    model.fc=torch.nn.Linear(model.fc.in_features,num_classes)
    return model

if __name__=="__main__":
    model=build_resnet(num_classes=2,pretrained=False)
    print(model.fc)
    print("Only the final classifier layer is trainable.")
