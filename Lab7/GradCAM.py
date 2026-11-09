"""Grad-CAM utility for CNNs (requires a trained model and input tensor)."""
import torch
import torch.nn.functional as F

class GradCAM:
    def __init__(self, model, target_layer):
        self.model=model; self.target_layer=target_layer
        self.activations=None; self.gradients=None
        target_layer.register_forward_hook(self._forward_hook)
        target_layer.register_full_backward_hook(self._backward_hook)
    def _forward_hook(self,module,input,output):
        self.activations=output
    def _backward_hook(self,module,grad_input,grad_output):
        self.gradients=grad_output[0]
    def __call__(self,input_tensor,class_index):
        output=self.model(input_tensor)
        self.model.zero_grad()
        output[:,class_index].sum().backward()
        weights=self.gradients.mean(dim=(2,3),keepdim=True)
        cam=(weights*self.activations).sum(dim=1,keepdim=True)
        cam=F.relu(cam)
        cam=F.interpolate(cam,size=input_tensor.shape[-2:],mode="bilinear",align_corners=False)
        cam=cam-cam.min()
        cam=cam/(cam.max()+1e-8)
        return cam.detach()

# Example:
# model = torchvision.models.resnet18(weights=None)
# cam = GradCAM(model, model.layer4[-1])
# heatmap = cam(torch.randn(1,3,224,224), class_index=0)
