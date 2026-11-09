"""FGSM adversarial example demonstration using a small synthetic PyTorch model."""
import torch

def fgsm_attack(image, epsilon, data_grad):
    perturbed=image + epsilon*data_grad.sign()
    return torch.clamp(perturbed,0,1)

if __name__=="__main__":
    # Demonstration input and gradient; replace with a real trained image classifier.
    image=torch.rand(1,3,32,32)
    image.requires_grad=True
    model=torch.nn.Sequential(torch.nn.Flatten(),torch.nn.Linear(3*32*32,10))
    target=torch.tensor([2])
    loss=torch.nn.CrossEntropyLoss()(model(image),target)
    model.zero_grad(); loss.backward()
    adversarial=fgsm_attack(image.detach(),0.03,image.grad)
    print("Input range:",image.min().item(),image.max().item())
    print("Adversarial range:",adversarial.min().item(),adversarial.max().item())
    print("Perturbation L-infinity:",(adversarial-image.detach()).abs().max().item())
